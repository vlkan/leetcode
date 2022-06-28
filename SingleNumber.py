class Solution(object):
    def singleNumber(self, nums):
        """
        bit manupilation
        """
        xor = 0
        for num in nums:
            xor ^= num
        return xor