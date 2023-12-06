from typing import List

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        target = -1
        nums_length = len(nums)
        if nums_length == 1:
            return 0

        for index, num in enumerate(nums):
            if index == 0:
                right = sum(nums[index+1:])
                if right == 0:
                    target = index
                    return target
                
            elif index == nums_length:
                left = sum(nums[:index-1])
                if left == 0:
                    target = index
                    return target
                
            else:
                left = sum(nums[:index])
                right = sum(nums[index+1:])
                if left == right:
                    target = index
                    return target
                else:
                    continue
        return target

    def findMiddleIndex2(self, nums: List[int]) -> int:
        target = -1
        for index, num in enumerate(nums):
            left = sum(nums[:index])
            right = sum(nums[index+1:])
            if left == right:
                target = index
                return target
        return target
    
    def findMiddleIndex3(self, nums:List[int]) -> int:
        # 效率最高 NICE 利用左边右边相等，也就是一直统计左边的就可以，
        sum_nums = sum(nums)
        len_nums = len(nums)
        left_sum = 0
        for i in range(len_nums):
            flag = left_sum * 2 + nums[i]
            if flag == sum_nums:
                return i
            left_sum += nums[i]
        return -1

def test_solution():#
    s = Solution()
    case1 = [1, 7, 3, 6, 5, 6]
    assert s.findMiddleIndex(case1) == 3
    case2 = [1, 2, 3]
    assert s.findMiddleIndex(case2) == -1
    case3 = [2, 1, -1]
    assert s.findMiddleIndex(case3) == 0
    print("pass successfully")


if __name__ == '__main__':
    test_solution()