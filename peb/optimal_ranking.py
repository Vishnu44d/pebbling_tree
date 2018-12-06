#from visible_edge import find_visible_edges
#from test_graph import adj_list, unweighted_graph
from .test_graph import *

import collections

def leafs(adj_list):
    leafs_ = []
    level = 0
    for vertex in adj_list:
        if len(adj_list[vertex] == 1):
            leafs_.append(vertex)
    return leafs_

def breadth_first_search(graph, root): 
    visited, queue = set(), collections.deque([root])
    j = 0
    ls_in_bfs = []
    while queue: 
        j += 1
        vertex = queue.popleft()
        ls_in_bfs.append(vertex)
        for neighbour in graph[vertex]: 
            if neighbour not in visited: 
                visited.add(neighbour) 
                queue.append(neighbour) 
    print(ls_in_bfs)



if __name__ == '__main__':
    graph = unweighted_graph(adj_list)
    breadth_first_search(graph, 'A')
    #breadth_first_search(graph, 0)
