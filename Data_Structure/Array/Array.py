class Array:
    def __init__(self):
        self.data = {}
        self.length = 0

    def __repr__(self):
        return f"{self.data}"

    def ind(self, i):
        return self.data.get(i)

    def push(self, d):
        self.data[self.length] = d
        self.length += 1

    def pop(self):
        del(self.data[self.length-1])
        self.length -= 1
        return self.length

    def delAtInd(self, l):
        item = self.data[l]
        for g in range(l, self.length-1):
            self.data[g] = self.data[g+1]
        del(self.data[self.length-1])
        self.length -= 1
        print(item)

    def remove(self, k):
        for i in self.data.keys():
            if self.data[i] == k:
                self.delAtInd(i)
                break



a1 = Array()
print(a1.length)
a1.push('Hello')
a1.push('How')
a1.push('Are')
a1.push('You')
a1.push('?')
# print(a1.pop())
print(a1)
# print(a1.length)
# a1.delAtInd(2)
# print(a1.length)
a1.remove('How')
print(a1)






