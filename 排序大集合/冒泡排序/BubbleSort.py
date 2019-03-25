# !/usr/bin/python
# -*- coding:utf-8 -*-


# 冒泡排序

class Solution:
    def bubbleSort(self, n):
        flag = len(n)
        while flag:
            for i in range(flag-1):
                if n[i] > n[i+1]:
                    n[i], n[i+1] = n[i+1], n[i]
            flag -= 1
        return n


if __name__ == '__main__':
    n = [5,11,9,1,2,3,6,2]
    print("Before n:", n)
    test = Solution()
    test.bubbleSort(n)
    print("after sorted n:", n)