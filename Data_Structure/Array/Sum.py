"""

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to 
target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

"""

from itertools import permutations as pe


def twoSums(nums: list[int], target: int) -> list[int]:
    ind = []
    per_num = pe(nums, 2)
    for i in per_num:
        if sum(i) == target:
            for x, y in enumerate(nums):
                if y in i:
                    ind.append(x)
            return ind


print(twoSums([3, 4, 6, 2], 8))
