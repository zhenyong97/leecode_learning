# 选择排序
import random

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


# 写一起
def selection_sort(alist):
    n = len(alist)
    # 需要进行n-1次选择操作
    for i in range(n-1):
        # 记录最小位置
        min_index = i
        # 从i+1位置到末尾选择出最小数据
        for j in range(i+1, n):
            if alist[j] < alist[min_index]:
                min_index = j
        # 如果选择出的数据不在正确位置，进行交换
        if min_index != i:
            alist[i], alist[min_index] = alist[min_index], alist[i]   



## 随机数组生成器
def generate_Narrays(n=1, length=5):
    for i in range(n):
        yield [random.randint(1,100) for n in range(length)]


if __name__ == "__main__":    
    N = 10000  # 测试次数
    flag = True
    for i in generate_Narrays(N, int(random.random()*10)):
        test1 = i.copy()
        test2 = i.copy()
        # 排序
        selection_sort(test1)
        test2.sort()
        if test1 != test2:
            flag = False

    print("Nice!" if flag else "Fucking fuck")
