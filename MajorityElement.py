import numbers


class Solution(object):
    def majorityElement(self, nums):
        result = 0
        maxNumber = 0

        for num in nums:
            numbers[num] = 1 + numbers.get(num, 0)
            if numbers[num] > maxNumber:
                result = num
            maxNumber = max(maxNumber, numbers[num])
        return result

    def majorityElement2(self, nums):
        """Boyer Moore Algorithm"""
        result = 0
        count = 0

        for num in nums:
            if count == 0:
                result = num
            count += 1 if num == result else -1
        return result