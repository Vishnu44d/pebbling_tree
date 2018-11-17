from peb.tree.tree import Tree
from peb.test_graph import adj_list, unweighted_graph






def adj_to_tree(graph):
    tree = Tree()
    for vertex, i in zip(graph, range(len(graph))):
        if i == 0:
            tree.add_node(vertex)
        else:
            tree.add_node(vertex, graph[vertex][0])
    return tree



if __name__ == "__main__":
    graph = unweighted_graph(adj_list)
    adj_to_tree(graph).display("A")



