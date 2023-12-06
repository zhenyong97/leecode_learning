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

def test_solution():
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