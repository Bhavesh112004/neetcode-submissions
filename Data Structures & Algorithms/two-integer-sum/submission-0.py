class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i in range(len(nums)):
            current_number = nums[i]
            diff = target - current_number

            if diff in seen:
                return [seen[diff], i]  # Return the list directly

            seen[current_number] = i