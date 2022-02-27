from itertools import permutations as pe

def closestNumbers(arr):
    '''
    Count of all pairs in an Array with minimum absolute difference
    '''
    arr.sort()
    min_diff = float('inf')
    for i in range(len(arr) - 1):
        diff = arr[i + 1] - arr[i]
        if diff < min_diff:
            min_diff = diff
    pairs = []
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] == min_diff:
            pairs.append((arr[i], arr[i + 1]))
    return pairs


def faultyTransaction(numbers, threshold):
    '''
    Write a program to find the faulty transaction if number of transactions for one account number is more than the threshold value from the given list of strings.
    In the given list of strings, each string contains the sender account number, receiver account number and the amount of money transferred. All 3 are separated by space.
    If sender and receiver account are same, then it will be considered as a one transaction.
    Example: 
    arr = ["1 2 47", "2 1 27", "1 3 17", "2 3 11", "1 2 7", "1 2 38", "4 4 39"]
    Threshold = 2

    Output:
    List of all such account number in the ascending order.
    For above case - [1,2]
    '''
    temp_dict = {}
    temp_arr = []
    
    for i in numbers:
        temp = i.split()
        if temp[0] == temp[1]:
            if temp_dict.get(temp[0]):
                temp_dict[temp[0]] += 1
            else:
                temp_dict[temp[0]] = 1
            continue
        if temp_dict.get(temp[0]):
            temp_dict[temp[0]] += 1
        else:
            temp_dict[temp[0]] = 1
        if temp_dict.get(temp[1]):
            temp_dict[temp[1]] += 1
        else:
            temp_dict[temp[1]] = 1
    for key, value in temp_dict.items():
        if value > threshold:
            temp_arr.append(key)
    temp_arr.sort()
    return temp_arr


def largestSum(arr):
    '''
    Largest Sum Contiguous Subarray
    '''
    max_sum = arr[0]
    curr_sum = arr[0]
    for i in range(1, len(arr)):
        curr_sum = max(arr[i], curr_sum + arr[i])
        max_sum = max(max_sum, curr_sum)
    return max_sum


def weightCapacity(weights, maxCapacity):
    '''
    https://leetcode.com/discuss/interview-question/858129/roblox-oa-new-grad-2021
    '''
    n = len(weights)
    c = 0
    temp_arr = []
    while c <= n:
        temp = pe(weights, c)
        for i in list(temp):
            if sum(i) == maxCapacity:
                return sum(i)
            elif sum(i) < maxCapacity:
                temp_arr.append(sum(i))
        c += 1
    return max(temp_arr)


if __name__ == "__main__":
    a = [7, 3, 6, 9, 1, 2, 4, 5, 8]
    print("closest pair - ", closestNumbers(a))
    print("faulty txn - ", faultyTransaction(["1 2 47", "2 1 27", "1 3 17", "2 3 11", "1 2 7", "1 2 38", "4 4 39"], 3))
    print("largest sum - ", largestSum([-2, -3, 4, -1, -2, 1, 5, -3]))
    print("weight capacity - ", weightCapacity([1, 3, 5], 7))