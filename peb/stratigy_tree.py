
'''
    The stratigy tree looks like this:
        tree = {
            (a,b):[(c,d), (e,f)],
            (g,h):[(i,j), (k,l), (l,m)],
        }
'''



class Tree(object):
    def __init__(self):
        self.left = None
        self.child = []
        self.data = []
 
    def setChildrenValues(self,list):
        for i in range(0,len(list)):
            self.data.append(list[i])
 
root = Tree()
#root.createChildren(3)
root.setChildrenValues([5,6,7]) 
 
root.child[0].createChildren(2)
root.child[0].setChildrenValues([1,2])
 
# print some values in the tree
print(root.data[0])
print(root.child[0].data[0])

'''
def generate_stratigy_tree(graph, root):
    empty_tree = {}
    for vertex in graph:
        empty_tree[(root, graph[vertex][0])].append(2)
     '''