class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        seen = {}

        # Count frequency
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1

        # Store [frequency, number]
        freq_list = []

        for num in seen:
            freq_list.append([seen[num], num])

        # Sort by frequency descending
        freq_list.sort(reverse=True)

        result = []

        # Take first k numbers
        for i in range(k):
            result.append(freq_list[i][1])

        return result