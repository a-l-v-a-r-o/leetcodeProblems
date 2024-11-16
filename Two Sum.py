"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution(object):

    def twoSumReturnIndex(self, nums, target):
        """
        :type nums: List[int]:type target: int:rtype: List[int]
        """
        num_dictionary = {}
        for i, num in enumerate(nums):
            complementary = target - num
            if complementary in num_dictionary:
                return [num_dictionary[complementary], i]
            num_dictionary[num] = i
        return []

    def twoSumReturnNumber(self, nums, target):
        """
        :type nums: List[int]:type target: int:rtype: List[int]
        """
        num_list = []
        contador = 0
        while contador < len(nums):
            for num in nums:
                complement = target - num
                if complement in num_list:
                    return [complement, num]
                num_list.append(num)
            return []

    def test(self):
        print(self.twoSumReturnIndex([2, 7, 11, 15], 9))
        print(self.twoSumReturnNumber([2, 7, 11, 15], 9))

Solution().test()