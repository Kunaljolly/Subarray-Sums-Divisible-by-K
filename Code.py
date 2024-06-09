class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        running_sum = 0
        prefix_sum = {0: 1}  # Initialize with a sum of 0 occurring once

        for num in nums:
            running_sum = (running_sum + num) % k
            # Ensure the remainder is positive
            running_sum = (running_sum + k) % k
            # Add the number of times the same remainder has been seen before
            count += prefix_sum.get(running_sum, 0)
            # Increment the count of this remainder
            prefix_sum[running_sum] = prefix_sum.get(running_sum, 0) + 1

        return count
