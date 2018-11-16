def bfs(s, adjacency_list):             # Taking the input s as initial state(node), and adjacency_list as dictionary
    level = {s: 0}
    parent = {s: None}
    i = 1
    frontier = [s]
    while frontier:
        next_level = []
        for u in frontier:
            for v in adjacency_list[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next_level.append(v)
        frontier = next_level
        i += 1
    return parent, level

'''
I need to write the code for checking above algorithm.
The return statement in the above function is written to check.

'''
s = 'A'
adjacency_list = {'A': ['B', 'C'],
                  'B': ['A', 'D', 'E'],
                  'C': ['A', 'F'],
                  'D': ['B'],
                  'E': ['B', 'F'],
                  'F': ['C', 'E']}




adj_list = {
    'A': [('B', 4), ('C', 1), ('D', 5)],
    'B': [('A', 4), ('E', 3), ('F', 1)],
    'C': [('A', 1), ('G', 3)],
    'D': [('A', 5), ('H', 4)],
    'E': [('B', 3), ('I', 1), ('J', 2)],
    'F': [('B', 1)],
    'G': [('C', 3), ('K', 1), ('L', 2)],
    'H': [('D', 4), ('M', 1), ('N', 2), ('O', 3)],
    'I': [('E', 1)],
    'J': [('E', 2)],
    'K': [('G', 1)],
    'L': [('G', 2)],
    'M': [('H', 1)],
    'N': [('H', 2)],
    'O': [('H', 3)]
}




print(bfs(s, adj_list))
