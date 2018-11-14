from visible_edge import find_visible_edges

import collections

def is_leaf(vertex):
    if len(adj_list[vertex] == 1):
        return True
    return False

ds = {v:i for v, i in zip(list(adj_list.keys()), range(len(adj_list)))}

def breadth_first_search(graph, root): 
    visited, queue = set(), collections.deque([root])
    j = 0
    while queue: 
        j += 1
        vertex = queue.popleft()
        if is_leaf(vertex):
            ds[vertex] = leaf_rankings[j]
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
