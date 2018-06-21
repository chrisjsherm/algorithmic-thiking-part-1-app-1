"""
Answer the questions for Module 1 Application of Algorithmic Thinking Part 1.
"""
import load_graph_data
import utility_graph
import random


def question_1():
    """
    Compute the in-degree distribution of the physics citation graph.
    Render a log/log plot of the points in the normalized distribution.
    """
    citation_graph = load_graph_data.load_graph(load_graph_data.CITATION_URL)

    in_degree_dist = utility_graph.in_degree_distribution(citation_graph)

    normalized_in_dist = utility_graph.normalize_distribution(in_degree_dist)

    utility_graph.plot_log_log_scatter(normalized_in_dist,
                                       'Physics Citations In-degree Distribution',
                                       'in-degree log-base-10', 'distribution log-base-10')


def question_2():
    """
    Compute in-degree distribution of an ER algorithm graph for comparison with
    the physics citation graph.
    """
    comparison_graph = er_algorithm(1000, random.uniform(0, 1))
    in_degree_dist = utility_graph.in_degree_distribution(comparison_graph)
    normalized_dist = utility_graph.normalize_distribution(in_degree_dist)

    utility_graph.plot_log_log_scatter(normalized_dist,
                                       'ER Algorithm In-degree Distribution',
                                       'in-degree log-base-10',
                                       'normalized distribution log-base-10')


def question_3():
    """
    Run the DPA algorithm to identify values for 'n' and 'm' that yield a graph
    whose number of nodes and edges is roughly the same as the citation graph.
    """
    citation_graph = load_graph_data.load_graph(load_graph_data.CITATION_URL)
    node_count = len(citation_graph)
    avg_out_degree = int(
        round(utility_graph.average_out_degree(citation_graph)))
    print('Node count for DPA graph: ' + str(node_count))
    print('Number of existing nodes to which a new node is connected: ' + str(avg_out_degree))

    comparison_graph = dpa_algorithm(node_count, avg_out_degree)
    in_degree_dist = utility_graph.in_degree_distribution(comparison_graph)
    normalized_dist = utility_graph.normalize_distribution(in_degree_dist)

    utility_graph.plot_log_log_scatter(normalized_dist,
                                       'DPA Algorithm In-degree Distribution',
                                       'in-degree log-base-10',
                                       'normalized distribution log-base-10')


def er_algorithm(node_count, p, is_directed_graph=True):
    """
    Compute a graph given the number of nodes in the graph and the probability
    each pair of nodes is connected.

    :param node_count: Number of nodes in the graph.
    :param p: Probability that two nodes are connected.
    :param is_directed_graph: Indicates whether the resulting graph should have
        directed or undirected edges.
    :returns: Dictionary representation of the graph, with each key an integer
    representing the node and each value a set respresenting the in node
    edges.
    """
    node_list = [node for node in xrange(node_count)]
    graph_dict = {}
    for node in node_list:
        graph_dict[node] = set()
        potential_edges = node_list[0:node] + node_list[node + 1:]
        for edge in potential_edges:
            a = random.uniform(0, 1)
            if a < p:
                graph_dict[node].add(edge)

                # If the graph is not directed, we need the edge's adjacency
                # set to have a matching entry for node.
                if not is_directed_graph:
                    if not graph_dict[edge] in graph_dict:
                        # Edge is not yet in the dictionary. Add it.
                        graph_dict[edge] = set()
                    
                    graph_dict[edge].add(node)

    return graph_dict


def dpa_algorithm(node_count, m):
    """
    Create a directed graph of n nodes iteratively, where in each iteration a
    new node is created, added to the graph, and connected to a subset of
    existing nodes.
    Grow the graph by adding n - m nodes, where each new node is connected to
    m nodes randomply chosen from the set of existing nodes. An existing node
    may be chosen more than once in an iteration, but duplicates are eliminated.

    :param node_count: Final number of nodes in the graph.
    :param m: Number of existing nodes to which a new node is connected.
    :returns: Dictionary representation of the graph with each key an integer
    representing the node and each value a set representing the in-node edges.
    """
    dpa_graph = utility_graph.make_complete_graph(m)

    # Add each node to the list "in-degree count + 1" times.
    # In-degree count for each node is (m - 1).
    nodes_prob_by_in_degree = [node for node in xrange(m)
                               for dummy_idx in range((m - 1) + 1)]

    for idx in xrange(m, node_count):
        # The ID of the new node is the length of the graph keys.
        node_id = len(dpa_graph)
        new_node_edges = set()

        # Add "m" edges.
        for edge_idx in xrange(0, m):
            new_node_edges.add(random.choice(nodes_prob_by_in_degree))

        # Add the new node to the graph.
        dpa_graph[node_id] = new_node_edges

        # Add the new edges to the probability list to keep the probability of
        # randomly choosing a node equal to it's in-degree + 1.
        nodes_prob_by_in_degree.extend(new_node_edges)

        # Add the new node to the probability graph since the probability of
        # randomly choosing a node is equal to it's in-degree (which is
        # currently zero) + 1.
        nodes_prob_by_in_degree.append(node_id)

    return dpa_graph


question_3()
