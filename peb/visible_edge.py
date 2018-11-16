from test_graph import adj_list


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
    visible = find_visible_edges(adj_list)
    print(visible)
