"""
Today Omar has assignment problems from his math professor. Yes, Omar has infinite number of questions that he
must solve today. The first problem went something like this.

Given N integers in the form of A(i) where , Omar wants to make each number in the N numbers equal to M. To convert a
number to M, it will cost M-A(i) units. The problem asks to find out the minimum cost to convert all the N numbers to M,
so you should choose the best M to get the minimum cost.

Omar gets bored easily from these kind of questions, can you solve it for him ?

Input:

First line of the input contains an integer T denoting the number of test cases.
First line of every test-case contains an integer N.
Second line of every test case contains N space separated integers

.

Output:

For each case, print the minimum cost that Omar needs to pay to convert each
to M, in a separate line.

Sample Input

1
4
1 2 4 5

Sample Output

6

Explanation

One of the best M's you could choose in this case is 3.
So the answer --> |1 - 3|+|2 - 3|+|4 - 3|+|5 - 3| = 6
"""