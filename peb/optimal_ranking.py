
from .test_graph import *
from .tree.tree import Tree
import collections







def leafs(adj_list):
    leafs_ = []
    depth_below_it = 0
    for vertex in adj_list:
        if len(adj_list[vertex]) == 1:
            leafs_.append((vertex, depth_below_it))
    return leafs_

def breadth_first_search(graph, root): 
    visited, queue = set(), collections.deque([root])
    while queue: 
        vertex = queue.popleft()

        for neighbour in graph[vertex]: 
            if neighbour not in visited: 
                visited.add(neighbour) 
                queue.append(neighbour) 




if __name__ == '__main__':
    graph = unweighted_graph(adj_list)
    breadth_first_search(graph, 'A')
    #breadth_first_search(graph, 0)
