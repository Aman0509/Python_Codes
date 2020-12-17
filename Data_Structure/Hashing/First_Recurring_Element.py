# Google Question
# Given an array = [2,5,1,2,3,5,1,2,4]:
# It should return 2
#
# Given an array = [2,1,1,2,3,5,1,2,4]:
# It should return 1
#
# Given an array = [2,3,4,5]:
# It should return undefined or None


def firstRecurringElement(arr):
    d = {}
    for i in arr:
        if d.get(i) is None:
            d[i] = 1
        elif d.get(i):
            return i

    if sum(d.values()) == len(arr):
        return None


print(firstRecurringElement([2, 5, 1, 2, 3, 5, 1, 2, 4]))
print(firstRecurringElement([2, 1, 1, 2, 3, 5, 1, 2, 4]))
print(firstRecurringElement([2, 5, 5, 2, 3, 5, 1, 2, 4]))
print(firstRecurringElement([1, 2, 3, 4]))
