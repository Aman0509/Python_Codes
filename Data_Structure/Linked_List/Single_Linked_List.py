class Node:
    def __init__(self):
        self.data = None
        self.ref = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        return f"{self._display()[0]}"

    def _display(self):
        count = 0
        temp_list = []
        if self.head is None:
            return temp_list, count
        temp = self.head
        while temp is not None:
            temp_list.append(temp.data)
            count += 1
            temp = temp.ref
        return temp_list, count

    def transversal(self, ind):
        temp = self.head
        c = 0
        while c < ind - 1:
            temp = temp.ref
            c += 1
        return temp

    def length(self):
        return self._display()[1]

    def insert(self, data, pos=0):
        c = 0
        if self.head is None:
            n = Node()
            self.head = self.tail = n
            n.data = data
            n.ref = None
        else:
            if pos == 0:
                n = Node()
                n.ref = self.head
                self.head = n
                n.data = data
            elif 0 < pos <= self.length():
                temp = self.transversal(pos)
                n = Node()
                n.data = data
                n.ref = temp.ref
                temp.ref = n
            else:
                raise (IndexError, "Your index input is more than the length of Linked List")

    def del_at_index(self, ind):
        c = 0
        if self.head is None:
            return 'Linked List is Empty'
        else:
            if ind == 0:
                self.head = self.head.ref
            elif 0 < ind < self.length():
                temp = self.transversal(ind)
                if ind == self.length() - 1:
                    temp.ref = None
                    self.tail = temp
                else:
                    temp.ref = temp.ref.ref
                    temp.ref.ref = None
            else:
                raise (IndexError, "Your index input is more than the length of Linked List")

    def reverse(self):
        prev = None
        next = self.head
        while next is not None:
            temp = next.ref
            next.ref = prev
            prev = next
            next = temp
        self.head, self.tail = self.tail, self.head


o1 = SingleLinkedList()
o1.insert(12)
o1.insert(12)
o1.insert(12)
o1.insert(12)
o1.insert(34, 4)
o1.insert(67, 0)
o1.insert(89, 6)
print(o1)
o1.del_at_index(0)
o1.del_at_index(o1.length() - 1)
o1.del_at_index(3)
print("SLL - ", o1)
print("Length of SLL - ", o1.length())
o1.reverse()
print(o1)


# def insert(self, data, pos=0):
#     c = 0
#     if self.head is None:
#         n = Node()
#         self.head = self.tail = n
#         n.data = data
#         n.ref = None
#     else:
#         if pos == 0:
#             n = Node()
#             n.ref = self.head
#             self.head = n
#             n.data = data
#         elif 0 < pos <= self.length():
#             temp = self.head
#             while c < pos - 1:
#                 temp = temp.ref
#                 c += 1
#             n = Node()
#             n.data = data
#             n.ref = temp.ref
#             temp.ref = n
#         else:
#             raise (IndexError, "Your index input is more than the length of Linked List")
#
#
# def del_at_index(self, ind):
#     c = 0
#     if self.head is None:
#         return 'Linked List is Empty'
#     else:
#         if ind == 0:
#             self.head = self.head.ref
#         elif 0 < ind < self.length():
#             temp = self.head
#             while c < ind - 1:
#                 temp = temp.ref
#                 c += 1
#             if ind == self.length() - 1:
#                 temp.ref = None
#                 self.tail = temp
#             else:
#                 temp.ref = temp.ref.ref
#                 temp.ref.ref = None
#         else:
#             raise (IndexError, "Your index input is more than the length of Linked List")
