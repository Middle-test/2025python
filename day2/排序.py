import random
import time
import sys

sys.setrecursionlimit(1000000000)  # 递归深度限制


class Sort:   
    def __init__(self, n):
        """
        n是排序的数的个数
        :param n:
        """
        self.len = n
        self.arr = [0] * n
        self.random_data()

    def random_data(self):
        for i in range(self.len):
            self.arr[i] = random.randint(0, 99)

    def partition(self, left, right):
        """
        分区函数
        :param left:
        :param right:
        :return:
        """
        arr = self.arr
        i = k = left
        random_index = random.randint(left, right)
        arr[right], arr[random_index] = arr[random_index], arr[right]  # 避免陷入最坏情况
        for i in range(left, right):
            if arr[i] < arr[right]:  # 将小于pivot的数放到左边
                arr[i], arr[k] = arr[k], arr[i]
                k += 1
        arr[k], arr[right] = arr[right], arr[k]  # 将pivot放到中间
        return k

    def quick_sort(self, left, right):
        """
        快速排序
        :param left:
        :param right:
        :return:
        """
        if left < right:
            pivot = self.partition(left, right)
            self.quick_sort(left, pivot - 1)
            self.quick_sort(pivot + 1, right)

    def adjust_max_heap(self, pos, arr_len):
        """
        调整子树为大根堆
        :param pos:父亲节点的位置
        :param arr_len:当前堆的长度
        :return:
        """
        arr = self.arr
        dad = pos
        son = 2 * dad + 1
        while son < arr_len:
            if son + 1 < arr_len and arr[son + 1] > arr[son]:
                son += 1
            if arr[son] > arr[dad]:
                arr[son], arr[dad] = arr[dad], arr[son]
                dad = son
                son = 2 * dad + 1
            else:
                break

    def heap_sort(self):
        """
        把列表调整为大根堆
        :return:
        """
        for parent in range(self.len // 2 - 1, -1, -1):
            self.adjust_max_heap(parent, self.len)
        arr = self.arr
        arr[0], arr[-1] = arr[-1], arr[0]
        for arr_len in range(self.len - 1, 1, -1):
            self.adjust_max_heap(0, arr_len)
            arr[0], arr[arr_len - 1] = arr[arr_len - 1], arr[0]

    def time_sort(self, sort_func, *args, **kwargs):
        """
        测试排序算法的运行时间
        :param sort_func: 排序算法
        :return:
        """
        start_time = time.time()
        sort_func(*args, **kwargs)
        end_time = time.time()
        print("排序算法：{}，运行时间：{}秒".format(sort_func.__name__, end_time - start_time))


if __name__ == '__main__':
    my_sort = Sort(100000)
    # my_sort.quick_sort(0, 9)
    # my_sort.heap_sort()
    my_sort.time_sort(my_sort.quick_sort, 0, 99999)
    my_sort.time_sort(my_sort.heap_sort)
