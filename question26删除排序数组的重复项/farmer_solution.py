class Solution:
    def removeDuplicates(self, nums):
        for index, item in enumerate(nums):
            mark = nums.count(item)
            if mark == 1:
                pass
            else:
                for i in range(mark-1):
                    nums.pop(index)
        return len(nums)
		

if __name__ == '__main__':
    a = Solution()
    nums = [1,1,1,2,2,2,2,3,3,]
    a.removeDuplicates(nums)
    print(nums)