from graphviz import Digraph
import os
from peb.test_graph import adj_list

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

file_name = 'Example-1'
dot = Digraph(comment=file_name)
edges_ls = []

for v in adj_list.keys():
    dot.node(v, str(v))
    for i in adj_list[v]:
        edges_ls.append(str(v)+str(i[0]))

dot.edges(edges_ls)
dot.render('test-output/'+file_name+'.gv', view=True)
#print(edges_ls)
