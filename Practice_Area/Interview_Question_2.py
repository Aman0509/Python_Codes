# Write a function that returns whether a list of strings is sorted given a specific alphabet. A list of N words and the K-
# sized alphabet are given. 1 2 # input: words = ["cat", "bat", "tab"] 
# alphabet = ['c', 'b', 'a', 't']
# | alphbet| = K 
# | words | = N 
# output: True

def isorder(words, alphabet):
    st = ""
    ds = {alphabet[j]:j+1 for j in range(len(alphabet))}
    temp = []
    for i in words:
        for j in i:
            st += str(ds.get(j))
        temp.append(int(st))
        st = ""
    if sorted(temp) == temp:
        return True
    else: 
        return False
        
print(isorder(["cat", "cab", "tab"], ['c', 'b', 'a', 't']))
print(isorder(["cat", "bat", "tab"], ['c', 'b', 'a', 't']))