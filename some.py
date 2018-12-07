
class Node: 
	# constructor to create tree node 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None


def printPaths(root): 
	# list to store path 
	path = [] 
	printPathsRec(root, path, 0) 

# Helper function to print path from root 
# to leaf in binary tree 
def printPathsRec(root, path, pathLen): 
	
	# Base condition - if binary tree is 
	# empty return 
	if root is None: 
		return

	# add current root's data into 
	# path_ar list 
	
	# if length of list is gre 
	if(len(path) > pathLen): 
		path[pathLen] = root.data 
	else: 
		path.append(root.data) 

	# increment pathLen by 1 
	pathLen = pathLen + 1

	if root.left is None and root.right is None: 
		
		# leaf node then print the list 
		printArray(path, pathLen) 
	else: 
		# try for left and right subtree 
		printPathsRec(root.left, path, pathLen) 
		printPathsRec(root.right, path, pathLen) 

