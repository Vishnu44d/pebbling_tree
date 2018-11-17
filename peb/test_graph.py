#from optimal_ranking import breadth_first_search
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


def unweighted_graph(adj_list):
    new_g = {}
    for vertex in adj_list:
        new_g[vertex] = [i[0] for i in adj_list[vertex]]
    return new_g
    
if __name__ == "__main__":
    print(unweighted_graph(adj_list))
