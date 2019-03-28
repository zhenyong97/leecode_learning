# !/usr/bin/python
# -*- coding:utf-8 -*-

import random


class Solution:

    def insertion_sort(self, array):
        for i in range(len(array)-1):
            minIndex = i
            for n in range(i+1, len(array)):
                minIndex = n if array[n] < array[minIndex] else minIndex
            array[i], array[minIndex] = array[minIndex], array[i]



## 随机数组生成器
def generate_Narrays(n=1, length=5):
    for i in range(n):
        yield [random.randint(1,100) for n in range(length)]



if __name__ == '__main__':
    test = Solution()
    N = 10000  # 测试次数
    flag = True
    for i in generate_Narrays(N, int(random.random()*10)):
        test1 = i.copy()
        test2 = i.copy()
        # 排序
        test.insertion_sort(test1)
        test2.sort()
        if test1 != test2:
            flag = False

    print("Nice!" if flag else "Fucking fuck")
