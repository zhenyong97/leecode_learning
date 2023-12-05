from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sorted_dict = {}
        list_length = len(nums) + 1
        # sort
        for i in nums:
            sorted_dict[i] = i

        for i in range(list_length):
            num = sorted_dict.get(i, None)
            if num is None:
                return i
            
    def missingNumber2(self, nums: List[int]) -> int:
        # 使用set
        st = set(range(len(nums)+1))
        for i in nums:
            st.remove(i)
        return st.pop()


def test_solution():
    s = Solution()
    assert s.missingNumber([3, 0, 1 ]) == 2
    assert s.missingNumber([9,6,4,2,3,5,7,0,1]) == 8
    print("finished")


if __name__ == '__main__':
    test_solution()
