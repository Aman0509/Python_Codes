class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def print_tree(self, transversal_type):
        if self.root is None:
            print("Tree is Empty")
        elif transversal_type == "level":
            print(self._levelOrderTransversal())
        elif transversal_type == "inorder":
            print(self._inOrderTransversal(self.root))
        elif transversal_type == "preorder":
            print(self._preOrderTransversal(self.root))
        elif transversal_type == "postorder":
            print(self._postOrderTransversal(self.root))
        else:
            raise Exception("Invalid Transversal Type")

    def _levelOrderTransversal(self):
        queue = []
        s = ""
        queue.insert(0, self.root)
        while len(queue) > 0:
            s += str(queue[-1].data) + "->"
            temp_node = queue.pop()
            if temp_node.left:
                queue.insert(0, temp_node.left)
            if temp_node.right:
                queue.insert(0, temp_node.right)
        return s[0:-2]

    def _inOrderTransversal(self, node):
        temp = ""
        if node:
            self._inOrderTransversal(node.left)
            temp += str(node.data) + "->"
            self._inOrderTransversal(node.right)
        return temp[0:-2]

    def _preOrderTransversal(self, node):
        temp = ""
        if node:
            temp += str(node.data) + "->"
            self._preOrderTransversal(node.left)
            self._preOrderTransversal(node.right)
        return temp[0:-2]

    def _postOrderTransversal(self, node):
        temp = ""
        self._preOrderTransversal(node.left)
        self._preOrderTransversal(node.right)
        temp += str(node.data) + "->"
        return temp[0:-2]

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def arraytoBinary(self, arr):
        if self.root is None:
            self.root = Node(arr[0])
        for i in arr[1:]:
            self._add(i, self.root)

    def _add(self, val, node):
        if node.data > val:
            if node.left is None:
                node.left = Node(val)
            else:
                self._add(val, node.left)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self._add(val, node.right)

    def isPresent(self, val):
        if self.root is None:
            return None
        else:
            return True if self._search(val, self.root) else False

    def _search(self, val, node):
        if node.data == val:
            return True
        else:
            if node.data > val and node.left:
                """here we are returning the value of function which in turn return
                true if value is found from above conditional statement mentioned in 
                the beginning of this function"""
                return self._search(val, node.left)
            elif node.data < val and node.right:
                return self._search(val, node.right)

    def get_inorder_successor(self, node):
        n = node
        while n.left:
            n = n.left
        return n

    def delNode(self, val):
        if self.root is None:
            return None
        else:
            self._delNode(val, self.root)

    def _delNode(self, val, node):
        if val < node.data and node.left:
            node.left = self._delNode(val, node.left)
        elif val > node.data and node.right:
            node.right = self._delNode(val, node.right)
        else:
            if node.left and node.right:
                t = self.get_inorder_successor(node.right)
                node.data = t.data
                node.right = self._delNode(val, node.right)
            elif node.left:
                temp = node.left
                node = None
                return temp
            elif node.right:
                temp = node.right
                node = None
                return temp
            else:
                node = None
                return node
        return node


# ------------------------------------------------------------------------------

# t = BST()
temp_array = [100, 80, 200, 70, 90, 150, 300]
# for i in temp_array:
#     t.add(i)
# t.print_tree()
c = BST()
c.arraytoBinary(temp_array)
c.print_tree("inorder")
print(c.isPresent(80))
c.delNode(100)
c.print_tree("level")
