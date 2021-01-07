"""
Binary Tree Implementation using Linked List
"""


class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None


def create(arr, root, i, f):
    if i < f:
        temp_node = Node(arr[i])
        root = temp_node
        root.left = create(arr, root.left, 2 * i + 1, f)
        root.right = create(arr, root.right, 2 * i + 2, f)

    return root


def preOrderTransversal(root):
    if root:
        print(root.data, end=" ")
        preOrderTransversal(root.left)
        preOrderTransversal(root.right)


def inOrderTransversal(root):
    if root:
        inOrderTransversal(root.left)
        print(root.data, end=" ")
        inOrderTransversal(root.right)


def postOrderTransversal(root):
    if root:
        postOrderTransversal(root.left)
        postOrderTransversal(root.right)
        print(root.data, end=" ")


def levelOrderTransversal(root):
    queue = []
    t = ""
    if root:
        queue.insert(0, root)
        while len(queue) > 0:
            t += str(queue[-1].data) + " "
            node = queue.pop()
            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)
    return t


def search(val, root):
    if root:
        tree = levelOrderTransversal(root)
        return str(val) in tree.split()
    return False


###############################
##### RUNNING ENVIRONMENT #####
###############################

preOrderTransversal(create([20, 100, 3, 50, 15, 250, 35, 222], None, 0, 8))
print()
inOrderTransversal(create([20, 100, 3, 50, 15, 250, 35, 222], None, 0, 8))
print()
postOrderTransversal(create([20, 100, 3, 50, 15, 250, 35, 222], None, 0, 8))
print()
print(levelOrderTransversal(create([20, 100, 3, 50, 15, 250, 35, 222], None, 0, 8)))
print()
print(search(100, create([20, 100, 3, 50, 15, 250, 35, 222], None, 0, 8)))
