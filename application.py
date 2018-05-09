"""
Answer the questions for Module 1 Application of Algorithmic Thinking Part 1.
"""
import load_graph_data
import utility_graph

def question_1():
    citation_graph = load_graph_data.load_graph(load_graph_data.CITATION_URL)

    in_degree_dist = utility_graph.in_degree_distribution(citation_graph)

    
