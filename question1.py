class Solution_1:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [0, 1]
# time: 6376 ms, memory: 14.5 MB


class Solution_2:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            if (target - nums[i]) in nums[i + 1:]:
                j = nums[i + 1:].index(target - nums[i])
                return [i, i + j + 1]
        return [0, 1]
# time: 868 ms, memory: 14.9 MB


class Solution_3:
    def twoSum(self, nums, target):
        Hash = {}
        for i, v in enumerate(nums):
            Hash[v] = i
        for i in range(len(nums)):
            j = Hash.get(target - nums[i])
            if j is not None and j != i:
                return [i, j]
# time: 60 ms, memory: 15.7 MB


if __name__ == "__main__":
    s = Solution_3()
    nums = [2, 15, 11, 15]
    target = 30
    print(s.twoSum(nums, target))


