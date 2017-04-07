#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
在一个二维数组中，每一行都按照从左到右递增的顺序排序
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

'''
书上说，有经验的程序员一眼就能看书是二分查找的思想(┗ 或者┓部分)，好惭愧
查找方式从右上角开始查找
如果当前元素大于target, 左移一位继续查找
如果当前元素小于target, 下移一位继续查找
进行了简单的修改, 可以判定输入类型为字符的情况
'''

'''
延伸：
如果出现了array中既有字符串,又有数字,可能需要用到ord()函数
'''


class Solution(object):
    '''Solution'''
    def find(self, arr, target):
        '''find target from array'''
        # 判断数据是否为空，知识点：is 和 == 有什么区别
        if arr == []:
            return False

        row = len(arr)
        col = len(arr[0])
        i_row = 0
        j_col = col - 1

        while True:
            if arr[i_row][j_col] == target:
                return True
            elif arr[i_row][j_col] < target:
                i_row += 1
            else:
                j_col -= 1

            if i_row > row - 1 or j_col < 0:
                return False


if __name__ == '__main__':
    arr1 = [
        [1, 2, 3, 5],
        [2, 3, 5, 6],
        [3, 7, 8, 9],
        [5, 8, 11, 12]
    ]

    solution = Solution()
    print solution.find(arr1, 4)
    print solution.find(arr1, 7)
    print solution.find(arr1, 17)
    print solution.find(arr1, 10)
    arr2 = []
    print id(arr2)
    print solution.find(arr2, 10)
