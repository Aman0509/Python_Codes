"""
Binary Tree Implementation using Linked List
"""


class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None


def create(arr, root, i, f):
    """We are creating tree using python list"""
    if i < f:
        temp_node = Node(arr[i])
        root = temp_node
        root.left = create(arr, root.left, 2 * i + 1, f)
        root.right = create(arr, root.right, 2 * i + 2, f)

    return root


def maxdepth(node):
    if node is None:
        return 0
    else:
        leftDepth = maxdepth(node.left)
        rightDepth = maxdepth(node.right)
    return max(leftDepth, rightDepth) + 1


def preOrderTransversal(root):
    if root:
        print(root.data, end=" ")
        preOrderTransversal(root.left)
        preOrderTransversal(root.right)


def inOrderTransversal(root):
    if root:
        inOrderTransversal(root.left)
        # print(root.data, end=" ")
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


def search(root, val):
    if root:
        tree = levelOrderTransversal(root)
        return str(val) in tree.split()
    return False


def insert(root, val):
    queue = []
    if root:
        queue.insert(0, root)
        temp_node = Node(val)
        while len(queue) > 0:
            node = queue.pop()
            if node.left:
                queue.insert(0, node.left)
            else:
                node.left = temp_node
                break
            if node.right:
                queue.insert(0, node.right)
            else:
                node.right = temp_node
                break
    else:
        node = Node(val)
        return node.data


def delbinarytree(root):
    root = None


def delNode(root, val):
    queue = []
    temp = None
    node = None
    if root:
        queue.insert(0, root)
        while len(queue) > 0:
            if queue[-1].data == val:
                temp = queue[-1]
            node = queue.pop()
            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)

        if temp:
            temp.data = node.data
            dellastnode(root, node)


def dellastnode(root, node):
    queue = []
    temp = None
    if root:
        queue.insert(0, root)
        while len(queue) > 0:
            temp_node = queue.pop()
            if temp_node.left:
                if temp_node.left == node:
                    temp_node.left = None
                    break
                else:
                    queue.insert(0, temp_node.left)
            if temp_node.right:
                if temp_node.right == node:
                    temp_node.right = None
                    break
                else:
                    queue.insert(0, temp_node.right)


###############################
##### RUNNING ENVIRONMENT #####
###############################

bin_tree = create([20, 100, 3, 50, 15, 250, 35, 222], None, 0, 8)
# preOrderTransversal(bin_tree)
# print()
# inOrderTransversal(bin_tree)
# print()
# postOrderTransversal(bin_tree)
# print()
# print(levelOrderTransversal(bin_tree))
# print()
# print(search(bin_tree, 100))
# insert(bin_tree, 45)
# insert(bin_tree, 2345)
# insert(bin_tree, 179)
# print()
print(levelOrderTransversal(bin_tree))
delNode(bin_tree, 3)
print(levelOrderTransversal(bin_tree))


