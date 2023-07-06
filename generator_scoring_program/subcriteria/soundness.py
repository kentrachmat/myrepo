from .base import *

import time
import arxiv
import scipy
import requests
import numpy as np
import bibtexparser
from sentence_transformers import SentenceTransformer
from bs4 import BeautifulSoup

# For c1 we will use as reference citations that are created by a languages model for the text of the original papers (not providing it the real citations)

# For c2 we will use as reference the citations of another real paper form the same topic (but not the same prompt.)

# For c3 we will compare pairwise the abstract of the cited papers of the original paper and use as reference pairwise comparisons in abstracts of papers generated by an LLM to summarize the original paper.

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
model_name = 'paraphrase-MiniLM-L6-v2'
model = SentenceTransformer(model_name)
TRESHOLD = 0.5
class Soundness(Base):
	def __init__(self):
		super().__init__()
		
	def get_call_semantic(self, title):
		headers = {
			"x-api-key": "GYY0JXc5a1ax4IOsJ5giU5HTfRPplPoe8ZYddU4a"
		}
		url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={title}&limit=10&fields=url,authors,abstract,title,year"
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			return response.json()
		elif response.status_code == 429:
			time.sleep(5)
			return self.get_call_semantic(title)
		
	def get_paperinfo(self, paper_url):
		response=requests.get(paper_url,headers=headers)
		if response.status_code != 200:
			print('Status code:', response.status_code)
			raise Exception('Failed to fetch web page ')

		paper_doc = BeautifulSoup(response.text,'html.parser')
		return paper_doc

	def get_tags(self, doc):
		paper_tag = doc.select('[data-lid]')
		# link_tag = doc.find_all('h3',{"class" : "gs_rt"})
		abstract_tag = doc.find_all("div", {"class": "gs_rs"})
		# author_tag = doc.find_all("div", {"class": "gs_a"})

		return paper_tag,abstract_tag

	def get_papertitle(self, paper_tag):
		paper_names = []
		for tag in paper_tag:
			paper_names.append(tag.select('h3')[0].get_text())
		return paper_names

	def get_abstract(self, abstract_tag):
		paper_names = []
		for tag in abstract_tag:
			paper_names.append(tag.get_text())
		return paper_names

	def get_call_google_scholar(self, title):
		query = title.replace(" ","+")
		query = query.replace(":","%3A")
		query = query.replace("&","%26")
		query = query.replace(",","%2C")
		query = query.replace("/","%2F")
		

		url = f"https://scholar.google.com/scholar?&q={query}+&hl=en&as_sdt=0,5&oq=o"
		try:
			doc = self.get_paperinfo(url)
			paper_tag,abstract_tag = self.get_tags(doc)

			papername = self.get_papertitle(paper_tag)
			abstract = self.get_abstract(abstract_tag)
			return [papername[0], abstract[0]]
		except Exception as e:
			return []

	def get_evaluation_c1(self, data_original):
		good = []
		bad = []
		bib_database = bibtexparser.loads(data_original[-1]['text'])

		for entry in bib_database.entries:
			if 'title' in entry: #  and 'author' in entry and 'year' in entry
				title = entry['title']
				# authors = entry['author']
				# year = entry['year']

				datas = self.get_call_semantic(title)
				if datas == None or datas['total'] == 0:
					arr = self.get_call_google_scholar(title)
					if arr != []:
						good.append({"title":arr[0],"abstract":arr[1]})
					else:
						print("[BAD 1: scholar not found] ", title)
						bad.append(title)
						continue

				if 'data' in datas and len(datas['data']) > 0:
					title_list = []
					for data in datas['data']:
						title_list.append(data['title'])

					sentence_embeddings = model.encode(title_list)
					query_embedding = model.encode([title])
					distances = scipy.spatial.distance.cdist(query_embedding, sentence_embeddings, "cosine")[0]
					results = [1-d for d in distances]
					results = sorted(results, reverse=True)

					if results[0] >= TRESHOLD:
						good.append(data)
					else:
						arr = self.get_call_google_scholar(title)
						if arr != []:
							good.append({"title":arr[0],"abstract":arr[1]})
						else:
							print("[BAD 2: scholar not found after SS] ", title)
							bad.append(title)

				else:
					bad.append(title)
					# print("ERROR:", self.get_call_semantic(title))
					# print(type(e),str(e))
					continue

			else:
				bad.append(title)
				print("[BAD 3: Format wrong] ", title)

		time.sleep(0.15)
		return (min(len(good), 10) - min(len(bad), 10))/10, good, bad

	def get_evaluation_c2(self, data_original, good):
		ref_goods = []
		for g in good:
			ref_goods.append(f"{g['title']}. {g['abstract']}")

		sentence_embeddings = model.encode(ref_goods)

		queries = [f"{data_original[0]['text']}. {data_original[1]['text']}"]
		query_embedding = model.encode(queries)
		data_c2 = []

		distances = scipy.spatial.distance.cdist(query_embedding, sentence_embeddings, "cosine")[0]
		results = [1-d for d in distances]
		results = sorted(results, reverse=True)

		for res in results:
			data_c2.append(max(res,0))

		return np.mean(data_c2), sentence_embeddings
	
	def get_evaluation_c3(self, sentence_embeddings):
		data_c3 =[]
		for index, _ in enumerate(range(len(sentence_embeddings))):
			distances = scipy.spatial.distance.cdist(sentence_embeddings[index].reshape(1,-1), sentence_embeddings, "cosine")[0]
			results = [1-d for d in distances]
			results = sorted(results, reverse=True)
			for res in results:
				data_c3.append(abs(res))
		return 1 - np.mean(data_c3)

	def soundness_evaluation(self, c1,c2,c3):
		return (1+(c1*c2*c3))/2

	def get_evaluation(self, paper): 
		c1, good, bad = self.get_evaluation_c1(paper)
		
		if (len(good) == 0):
			c2,c3 = 0,0
		else :
			c2,sentence_embeddings = self.get_evaluation_c2(paper, good)
			c3 = self.get_evaluation_c3(sentence_embeddings)
		# print(c1,c2,c3, len(good), len(bad))
		return {"c1" : {"score":c1, "comment": "TEST"}, "c2" : {"score":c2, "comment": "TEST"}, "c3" : {"score":c3, "comment": "TEST"}}