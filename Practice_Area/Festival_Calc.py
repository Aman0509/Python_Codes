"""
Alice likes festivals a lot as we all do. He also likes spending money on these festivals. He spends money in
buying various things on these festivals. But he has problem of forgetting. He only remembers his top three maximum
spending for any festival. For eg, on Holi he spends 25 units on colors, 50 units on water sprays, 100 units on
gifts, 150 units on sweets but he remembers only his top 3 spending ,i.e., 50, 100 & 150. Now as the year ends he
wants to know the festival on which he spent most of his money that he can remember.

Input Format

First line contains an integer T, denoting number of test cases. Second line contains an integer N, denoting number
of spending in a year. Each of the next N lines contain a string S and an integer X denoting festival name and
spending on one of the events of that festival.

Output Format

For each test case, print a single line containing the festival name and its total spending that he remembers.
If there are more than 1 festival with the maximum spending, print the one which has lexicographically smallest name.

Sample Input
2
6
B 20
A 2
A 10
A 10
B 30
A 30
3
abc 10
xyz 15
oop 8

Sample Output

A 50
xyz 15

 Explanation

Test Case 1 :

Festival : A, He forgets 2 as he can remember only three max spending. So he remembers 10 + 10 + 30 = 50

Festival : B, He spent only two times i.e with 20 and 30 units. So he remembers 50 .

Since total spending for both festivals is same, we have to chose the festival with lexicographically smallest name.
So, our answer is 'A 50'.

Test Case 2:

Festival: abc - Amount spent - 10

Festival: xyz - Amount spent - 15

Festival: oop - Amount spent - 8

As spending on xyz are highest. So answer is 'xyz 15'.

"""

def calcspending(fs):
    d = {}
    temp = [i.split() for i in fs]
    for j in temp:
        if d.get(j[0]):
            d[j[0]].append(int(j[1]))
        else:
            d[j[0]] = []
            d[j[0]].append(int(j[1]))
    d1 = {k: sorted(v) for k, v in sorted(d.items(), reverse=True, key=lambda ele: ele[0])}
    for k, v in d1.items():
        s = sum(d1[k][-3:])
        d1[k] = s
    d2 = {v: k for k, v in d1.items()}
    return d2[max(d2)], max(d2)


# t = int(input())
# for i in range(t):
#     temp = []
#     n = int(input())
#     for j in range(n):
#         fs = input()
#         temp.append(fs)

print(calcspending(['B 20', 'A 10', 'A 2', 'B 30', 'A 10', 'A 30', 'C 20', 'C 10']))
print(calcspending(['abc 10', 'xyz 15', 'oop 8']))
