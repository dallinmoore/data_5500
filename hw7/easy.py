# Dallin Moore
# Ask ChatGPT:
# What is wrong with this code? ...
# Answer: `node.left = insert(node.right,key)` should be `node.left = insert(node.left,key)`

class Node:
	# Constructor to create a new node
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None
	
	# implement string method that returns the key
	def __str__(self):
	    return str(self.key)
	
		
def insert(node, key):
    if node is None:
        # return the key as a node if its not one
        return Node(key)
    
    if key < node.key:
        node.left = insert(node.left,key)
    else:
        node.right = insert(node.right,key)
    return node


# my_node = Node(8)
# my_node = insert(my_node,7)
# my_node = insert(my_node,1)

# print(my_node.left)