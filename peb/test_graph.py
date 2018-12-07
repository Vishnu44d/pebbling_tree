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


class Vertex: 
	# constructor to create tree node 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None


bt = {
    0 : [1, 2],
    1 : [0],
    2 : [0, 3, 4],
    3 : [2],
    4 : [2],
}

def n_tree(bt):
    n_adj_list = {}
    # (name_of_node, edge_ranking_above_it, depth_below_it)
    for v in bt:
        if len(bt[v]) == 1:
            #leaf node
            parent = bt[v][0]
            sibling = list(set(bt[parent][1:]) - set([v]))[0]
            if bt[sibling] == 1:
                ##means sibling is also leaf node
                n_adj_list[(v, 1, 0)]
            print(parent, v, sibling)
        n_adj_list[(v, 0, 0)] = [(i, 0, 0) for i in bt[v]]
    return n_adj_list






def unweighted_graph(adj_list):
    new_g = {}
    for vertex in adj_list:
        new_g[vertex] = [i[0] for i in adj_list[vertex]]
    return new_g
    
if __name__ == "__main__":
    #print(unweighted_graph(adj_list))
    print(n_tree(bt))
