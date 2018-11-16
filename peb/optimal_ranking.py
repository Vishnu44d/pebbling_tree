from visible_edge import find_visible_edges
from test_graph import adj_list
import collections

def leafs(adj_list):
    leafs_ = []
    for vertex in adj_list:
        if len(adj_list[vertex] == 1):
            leafs_.append(vertex)
    return leafs_

def breadth_first_search(graph, root): 
    visited, queue = set(), collections.deque([root])
    j = 0
    while queue: 
        j += 1
        vertex = queue.popleft()
        
        for neighbour in graph[vertex]: 
            if neighbour not in visited: 
                visited.add(neighbour) 
                queue.append(neighbour) 






if __name__ == '__main__':
    graph = {
        0: [1, 2],
        1: [3],
        2: [4],
        3: [],
        4: [5],
        5: [],
        6: []
    } 
    breadth_first_search(graph, 0)
    #breadth_first_search(graph, 0)
