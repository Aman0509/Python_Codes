class Hashtable:
    def __init__(self, size):
        self.data = [None for _ in range(size)]
        self.length = size

    def __str__(self):
        return str(self.data)

    def _hashFunction(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i])*i) % self.length
        return hash

    def set(self, key, value):
        address = self._hashFunction(key)
        if self.data[address] == None:
            self.data[address] = []
        self.data[address].append([key, value])
        return self.data

    def get(self, key):
        address = self._hashFunction(key)
        if self.data[address] is not None:
            for l in self.data[address]:
                if l[0] == key:
                    return l[1]
        else:
            return None

    def keys(self):
        allKeys = []
        for i in self.data:
            if i is not None:
                for j in i:
                    allKeys.append(j[0])
        return allKeys


obj1 = Hashtable(50)
obj1.set('grapes', 20)
obj1.set('grapes', 40)
obj1.set('apples', 25)
print(obj1.get('grapes'))
print(obj1)













