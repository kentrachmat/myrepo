"""
Sample predictive model (dummy).
You must supply at least 2 methods:
- generate_papers: generate a dummy template text
- review_papers: generate a random score for each paper
"""

import random
 
class model():
    def __init__(self):
       pass

    def generate_papers(self, prompts, _):
        """
        Arguments:
            prompts: list of strings 
        Returns:
            generated_papers: list of dictionaries
        """
        generated_papers = []
        for i in range(len(prompts)):
            template = [{
                    "heading": "Title",
                    "text": "Exploring Nature's Solutions: A Guide to Bio-Inspired Optimization Techniques"
                },
                {
                    "heading": "Abstract",
                    "text": "Bio-inspired optimization algorithms are computer science techniques that are inspired by natural biological evolution and the collective behavior of living organisms such as insects and animals. These algorithms are used to solve complex optimization problems and have gained popularity due to their diverse, robust, dynamic, and complex nature. This paper provides an overview of the taxonomy of bio-inspired optimization algorithms based on the biological field that inspired them and the areas where they have been successfully applied."
                },
                {
                    "heading": "Introduction",
                    "text": "The paper discusses the increasing complexity of real-life problems and the need for useful methods to find and optimize solutions for complex and optimization problems. Bio-inspired algorithms (BIA) have shown significant proficiency in solving many optimization problems and are broadly classified into three categories: evolutionary-based algorithms, swarm-based algorithms, and ecology-based algorithms. Evolutionary-based algorithms simulate natural biological evolution and social behavior to find optimal or near-optimal solutions to large-scale optimization problems. Swarm intelligence is concerned with designing and developing intelligent interactive multi-agent systems that cooperate to achieve a specific goal. Swarm-based algorithms are inspired by behaviors of social living beings in nature. Ecological-inspired algorithms depend on populations of individuals and each population develops according to a search strategy. The paper provides an overview of bio-inspired optimization algorithms and their classifications, biological inspirations, and successful applications."
                },
                {
                    "heading": "Bio-Inspired Algorithms (Bias) Taxonomy",
                    "text": "Real-world optimization problems are often complex and involve multi-objective optimization. Traditional deterministic algorithms cannot solve most of these problems, which are NP-hard. Bio-Inspired algorithms have been proven to be effective in addressing these complex optimization problems and have been applied to solve problems in various domains. Over the past few decades, various Bio-Inspired Algorithms have been developed, taking inspiration from different biological swarms that occur in nature. The performance of many global optimization techniques, such as genetic algorithms, depends mainly on the evolutionary settings of these algorithms. Effective optimization algorithms should minimize time, cost, and effort for solving complex optimization problems, handle non-differentiable, nonlinear and multimodal cost functions, be parallelizable to cope with computation-intensive cost functions, have good convergence properties, and be easy to use with few control variables that are robust and easy to choose. Figure (1) presents a graphical classification of some well-known Bio-Inspired Algorithms, and Table (1) shows the meaning of the abbreviations used in the figure."
                },
                {
                    "heading": "Evolutionary Algorithms (Ea)",
                    "text": "The paper discusses Evolutionary Algorithms (EAs), which are a type of nature-inspired algorithm that simulate biological evolution and social behavior of living species. EAs are widely used for solving complex optimization problems in various fields of science and real-time applications. The paper mentions that EAs are the most well-known and established algorithms among nature-inspired algorithms. The paper also lists some of the most well-known algorithms that belong to EAs, including Differential Evolution, Evolutionary Strategy, Genetic Algorithm, Genetic Programming, and Granular Agent Evolutionary Algorithm. The paper cites Holland's work from 1975 as a reference for EAs. Overall, the paper provides an overview of EAs and their applications in solving optimization problems."
                },
                {
                    "heading": "Genetic Algorithm (Ga)",
                    "text": "The genetic algorithm (GA) is a type of evolutionary computation algorithm used in artificial intelligence to solve optimization and search problems. It is part of a larger class of evolutionary algorithms (EA) that use techniques inspired by natural evolution, such as inheritance, mutation, selection, and crossover. GA mimics the reproduction behavior observed in biological populations and develops a population of initial individuals called chromosomes, where each chromosome denotes a solution to the problem to be solved. By applying recombination techniques such as crossover and mutation, GA attempts to find an optimal solution for a given problem. GA has been successfully applied to solve problems in various fields such as mathematics, computational science, bioinformatics, engineering, economics, and more. Figure (2) illustrates the procedure of how GA works."
                },
                {
                    "heading": "Evolutionary Strategy Es",
                    "text": "Evolution Strategy (ES) is a computer science optimization technique based on evolution and adaptation. It is a type of evolutionary computation that evolves individuals through mutation and recombination. ES algorithms are designed to solve problems in the real-value domain and use self-adaptation to adjust control parameters of the search. The procedure of how the Evolution Strategy Algorithm works is shown in Figure (3)."
                },
                {
                    "heading": "Swarm Intelligence Si",
                    "text": "Swarm Intelligence (SI) is a subfield of Artificial Intelligence (AI) that studies and designs computational systems consisting of multiple agents that work together to achieve a specific goal. The behavior of real-life swarms, such as birds, fish, and ants, is used to solve complex optimization problems. SI was introduced in 1989 by Jing Wang and Gerardo Beni as a collection of algorithms for controlling robotic swarms within the global optimization framework."
                },
                {
                    "heading": "Ant Colony Optimization Aco",
                    "text": "The Ant Colony Optimization (ACO) Algorithm is a heuristic algorithm that mimics the behavior of real ants in finding the shortest path between their current location and a source of food. Ants communicate with each other indirectly through pheromone trails, which they deposit and smell. In a swarm, each ant randomly lays down a pheromone trail on its way to a food source. If an ant finds a source of food, it returns to the nest by following the pheromone trail. If the pheromone level increases on a particular path, all the other ants follow that path. The ACO algorithm works by simulating this behavior of ants. The algorithm is useful in solving optimization problems, and it has been applied in various fields such as transportation, telecommunications, and manufacturing."
                },
                {
                    "heading": "Particle Swarm Optimization Pso",
                    "text": "The Particle Swarm Optimization (PSO) algorithm is based on the social behavior of organisms such as fishing, bird flocking, and schooling. It is a widely used optimization tool to solve computational problems, including NP-Hard problems like the Travelling Salesman Problem (TSP). PSO particles work together as a group to achieve their goal. The algorithm simulates this social behavior to solve optimization problems. The procedure for how the PSO algorithm works is shown in Figure 5."
                },
                {
                    "heading": "Elephant Herding Optimization Eho",
                    "text": "The Elephant Herding Optimization (EHO) algorithm is a type of swarm-based metaheuristic search method that is used to solve optimization problems. The algorithm is based on the herding behavior of real elephants in nature, where a population of elephants is divided into subgroups called clans, each led by a matriarch. Male calves leave their clan when they reach adulthood. The EHO algorithm is modeled after this behavior and is used to find optimal solutions to problems. Figure 6 shows the procedure for how the EHO algorithm works. The algorithm was first introduced by Wang in 2015 and has since been studied and improved upon by researchers such as Almufti in 2019."
                },
                {
                    "heading": "Ecological-Inspired Algorithm Eco",
                    "text": "The paper discusses how natural ecosystems can be used as a source of inspiration for designing and solving complex computer science problems. It highlights the interactions among living organisms and their abiotic environment, such as soil, air, and water. Ecological-inspired algorithms (ECO) are used to develop cooperative and intelligent algorithms based on the interactions among species in an ecosystem. ECO relies on populations of individuals, each of which develops according to a specific search strategy. The individuals in each population are modified based on diversification, intensification, and the initial parameters of the search strategy. The paper also mentions the use of ecological concepts, such as habitats, ecological relationships, and ecological successions, as inspiration for ECO. Overall, the paper suggests that natural ecosystems can provide valuable insights for developing innovative solutions to complex computer science problems."
                },
                {
                    "heading": "Biogeography Based Optimization Bbo",
                    "text": "The paper discusses Biogeography-Based Optimization (BBO) Algorithm, a global optimization algorithm inspired by the migration strategy of animals or other species. BBO is a population-based algorithm that uses the idea of immigration and emigration of species between habitats to solve optimization problems. In BBO, each habitat is considered as an individual and has its habitat suitability index (HSI) to show the efficiency of the individual. High-HSI habitats denote good solutions, and low-HSI habitats denote poor solutions. Solution features emigrate from high-HSI habitats to low-HSI habitats. BBO uses fitness to determine the immigration and emigration rates, and applications that use these ideas allow information sharing between candidate solutions. The paper also includes a figure that shows the procedure of how BBO works."
                },
                {
                    "heading": "Ps2O Algorithm",
                    "text": "The text enclosed within the XML tags describes a new optimization method called PS 2 O. This method is an extension of the basic Particle Swarm Optimization (PSO) algorithm and takes into account the symbiotic co-evolution between different species. The concept of symbiosis, which is the living together of organisms from different species, is a common technique in nature. PS 2 O is inspired by the co-evolution of symbiotic species in natural ecosystems and the heterogeneous interaction between species. The paper also includes a figure that shows the procedure of how the PS 2 O algorithm works."
                },
                {
                    "heading": "Conclusion",
                    "text": "Bio-inspired optimization techniques, such as evolutionary algorithms, swarm intelligence, and ecological-inspired algorithms, have emerged as powerful tools for solving complex optimization problems. These algorithms simulate natural biological evolution, social behavior, and interactions among species to find optimal or near-optimal solutions. They have been successfully applied in various fields, including mathematics, engineering, bioinformatics, and economics. These techniques offer advantages such as handling non-differentiable and multimodal cost functions, parallelizability, good convergence properties, and ease of use. The paper provides a comprehensive overview of the taxonomy of bio-inspired optimization algorithms, their biological inspirations, and successful applications. It also introduces new algorithms, such as PS2O, which extend existing methods by incorporating symbiotic co-evolution. The findings highlight the potential of nature-inspired algorithms to revolutionize problem-solving in computer science and open up exciting avenues for future research in optimizing complex systems."
                },
                {
                    "heading": "References",
                    "text": "@article{almufti2017using,\n  title={Using Swarm Intelligence for solving NPHard Problems},\n  author={Almufti, S},\n  journal={Academic Journal of Nawroz University},\n  year={2017}\n}\n\n@article{alroomi2006essential,\n  title={Essential Modifications on Biogeography-Based Optimization Algorithm},\n  author={Alroomi, A and Albasri, F and Talaq, M and Townsend, CR and Harper, JL},\n  journal={Blackwell Publishing},\n  year={2006}\n}\n\n@article{binitha2012survey,\n  title={A Survey of Bio inspired Optimization Algorithms},\n  author={Binitha, S and Sathya, SS},\n  journal={International Journal of Soft Computing and Engineering},\n  year={2012}\n}\n\n@article{chen2008optimization,\n  title={Optimization based on symbiotic multi-species coevolution},\n  author={Chen, H and Zhu, Y},\n  journal={Applied Mathematics and Computation},\n  year={2008}\n}\n\n@article{das2011differential,\n  title={Differential evolution: a survey of the state-of-the-art},\n  author={Das, S and Suganthan, PN},\n  journal={IEEE Trans.Evol. Comput},\n  year={2011}\n}\n\n@article{dorigo1996ant,\n  title={Ant system: optimization by a colony ofcooperating agents},\n  author={Dorigo, M and Maniezzo, V and Colorni, A},\n  journal={IEEE Trans. Syst. Man Cybern. B},\n  year={1996}\n}\n\n@article{dubey2014bio,\n  title={Bio-inspired optimisation for economic load dispatch: a review},\n  author={Dubey, H and Panigrahi, B and Pandit, M},\n  journal={International Journal Of Bio-Inspired Computation},\n  year={2014}\n}\n\n@book{goldberg1989genetic,\n  title={Genetic Algorithms in Search, Optimization, and Machine Learning},\n  author={Goldberg, DE},\n  year={1989},\n  publisher={Addison-Wesley}\n}\n\n@book{holland1975adaptation,\n  title={Adaptation in Natural and Artificial Systems},\n  author={Holland, JH},\n  year={1975},\n  publisher={University of Michigan Press}\n}\n\n@article{kumar2014parameter,\n  title={Parameter adaptive harmony search algorithm for unimodal and multimodal optimization problems},\n  author={Kumar, V and Chhabra, J and Kumar, D},\n  journal={Journal of Computational Science},\n  year={2014}\n}\n\n@article{li2007comparative,\n  title={A comparative study of three evolutionary algorithms for surface acoustic wave sensor wavelength selection},\n  author={Li, C and Heinemann, P},\n  journal={Sensors and Actuators B: Chemical},\n  year={2007}\n}\n\n@article{li2010solving,\n  title={Solving TSP by an ACO-and-BOA-based Hybrid Algorithm},\n  author={Li, Y},\n  journal={IEEE Press},\n  year={2010}\n}\n\n@book{may2007theoretical,\n  title={Theoretical Ecology: Principles and Applications},\n  author={May, RMC and Mclean, AR},\n  year={2007},\n  publisher={Oxford University Press}\n}"
                }]
            print("Generating paper", i+1, "out of", len(prompts))
            generated_papers.append(template)
        return generated_papers
    

    def review_papers(self, papers, _):
        """
        Arguments:
            papers: list of strings 
        Returns:
            review_scores: list of dictionaries of scores, depending on the instructions
        """
        review_scores = []

        for i in range(len(papers)):
            review_score = {'Responsibility': round(random.uniform(0, 1), 2),
                            'Soundness': round(random.uniform(0, 1), 2),
                            'Clarity': {
                                'Correct language': round(random.uniform(0, 1), 2),
                                'Explanations': round(random.uniform(0, 1), 2),
                                'Organization': round(random.uniform(0, 1), 2)
                            },
                            'Contribution': {
                                'Coverage': round(random.uniform(0, 1), 2),
                                'Abstract': round(random.uniform(0, 1), 2),
                                'Title': round(random.uniform(0, 1), 2),
                                'Conclusion': round(random.uniform(0, 1), 2)
                            },
                            'Overall': round(random.uniform(0, 1), 2),
                            'Confidence': round(random.uniform(0, 1), 2)
                            }
            print("reviewing paper", i+1, "out of", len(papers))
            review_scores.append(review_score)

        return review_scores