"""
s='aaaabbbccaa'   output = '4a3b2c2a'
"""

def output(s):
    n = len(s)
    temp = s[0]
    c = 1
    temp_str = ""
    for i in range(1, n):
        if s[i] == temp:
            c += 1
        else:
            temp_str += str(c)+s[i-1]
            c = 1
            temp = s[i]
    temp_str += str(c)+temp
    return temp_str


print(output('aaaabbbxccaaf'))