from peb.tree.tree import Tree

tree = Tree()

tree.add_node("0")  # root node
tree.add_node("1", "0")
tree.add_node("2", "0")
tree.add_node("3", "1")
tree.add_node("4", "1")
tree.add_node("5", "2")
tree.add_node("6", "2")
tree.add_node("7", "6")
tree.add_node("8", "6")
tree.add_node("9", "5")
tree.add_node("10", "5")
tree.display("0")



'''from peb.test_graph import adj_list
from peb.visible_edge import find_visible_edges

print(adj_list)'''
#print(find_visible_edges(adj_list))