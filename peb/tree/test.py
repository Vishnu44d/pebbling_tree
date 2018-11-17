from tree import Tree

(_ROOT, _DEPTH, _BREADTH) = range(3)


'''

            0
    1               2
3       4       5       6





'''







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


'''
print("***** DEPTH-FIRST ITERATION *****")
for node in tree.traverse("Harry"):
    print(node)
print("***** BREADTH-FIRST ITERATION *****")
for node in tree.traverse("0", mode=_BREADTH):
    print(node)

'''