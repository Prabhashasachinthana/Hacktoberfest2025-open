class Solution:
    def findLHS(self, nums):
        nums.sort()
        maxLength = 0
        current_length = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                current_length += 1
            elif nums[i] - nums[i - 1] == 1:
                prev_count = current_length
                current_length = 1
                j = i - 1
                while j >= 0 and nums[j] == nums[i - 1]:
                    j -= 1
                maxLength = max(maxLength, (i - j - 1) + current_length)
            else:
                current_length = 1
        return maxLength
