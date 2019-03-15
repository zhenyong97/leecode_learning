class Solution1:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        p1 = 0
        n = len(nums)
        for p2 in range(n):
            if nums[p1] != nums[p2]:
                p1 += 1
                nums[p1] = nums[p2]
        nums[p1 + 1:] = []
        return len(nums)
        

if __name__ == '__main__':
    a = Solution1()
    nums = [1,1,1,2,2,2,2,3,3,]
    a.removeDuplicates(nums)
    print(nums)