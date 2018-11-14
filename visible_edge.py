



Max_edge_ranking_possible = 99

def generate_edges(graph):
    edges = []
    for node in graph:
        try:
            for neighbour in graph[node]:
                edges.append((node, neighbour[0], neighbour[1]))
        except:
            pass
    return edges

def find_path(graph, start, end, w, path=[]):
    path = path + [(start, w)]
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            new_path = find_path(graph, node[0], end, node[1], path)
            if new_path:
                return new_path
            return None

def desc(l):
    seq = [i[1] for i in l]
    return all(earlier >= later for earlier, later in zip(seq, seq[1:]))

def find_visible_edges(graph):
    visible = []
    root = 'A'
    for node in graph.keys():
        path = find_path(graph, node, root, Max_edge_ranking_possible)
        if(desc(path) == True):
            try:
                visible.append(path[1][1])
            except:
                pass
    return visible




if __name__ == "__main__":
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

    visible = find_visible_edges(adj_list)
    print(visible)
