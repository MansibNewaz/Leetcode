# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Leetcode 1: https://leetcode.com/problems/two-sum/

def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashMap = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashMap:
            return [i, hashMap[complement]]
        hashMap[num] = i

    return []

# Time Complexity: O(N)
# Space Complexity: O(N)
