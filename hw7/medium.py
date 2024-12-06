# Dallin Moore

from easy import *

def search(node, search_key):
    if node is None:
        return False
    elif search_key == node.key:
        return True
    elif search_key < node.key:
        return search(node.left,search_key)
    else:
        return search(node.right,search_key)
        
        
# my_node = Node(8)
# my_node = insert(my_node,7)
# my_node = insert(my_node,1)
# my_node = insert(my_node,45)
# my_node = insert(my_node,11)
# my_node = insert(my_node,18)
# my_node = insert(my_node,34)
# my_node = insert(my_node,6)
# my_node = insert(my_node,0)

# print(search(my_node, 45))