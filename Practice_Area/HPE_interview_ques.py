"""
Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

Example: 1
Input: ["abc", "abcd", "abcdjfk"]
ans: "abc"

Example: 2
Input: ["abc", "def", "ghijk"]
ans: ""

1 - calculate
"""

def longest_common_prefix(str_list):
    if len(str_list) != 0:
        str_list.sort()
        if str_list[0] == str_list[-1][0:len(str_list[0])]:
            return str_list[0]
    return None
        

print(longest_common_prefix(["abc", "def", "ghijk"]), end="\n")
print(longest_common_prefix(["abc", "abcd", "abcdjfk"]), end="\n")

"""
# How many elements are duplicated
Input: [0, 1, 2, 3]
Output: 0

Input: [0, 1, 2, 3, 1, 1, 3]
Output: 2
"""

def duplicate_elements(num_list):
    temp_var = 0
    temp_dict = {}
    temp_list = []
    length = len(num_list)
    for i in range(length):
        if temp_dict.get(num_list[i]):
            temp_dict[num_list[i]] += 1
        else:
            temp_dict[num_list[i]] = 1
    for k,v in temp_dict.items():
        if v > 1:
            temp_var += 1
            temp_list.append(k)
    return temp_var, temp_list

print(duplicate_elements([0, 1, 2, 3, 1, 1, 3]))