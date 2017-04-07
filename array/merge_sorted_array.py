#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Given two sorted integer arrays nums1 and nums2,
merge nums2 into nums1 as one sorted array.
'''


class Solution(object):
    def merge(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        m = len(nums1)
        n = len(nums2)
        nums1.extend([None] * n)
        print nums1

        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1

        if n > 0:
            nums1[:n] = nums2[:n]


if __name__ == '__main__':
    list_a = [1, 3, 5, 7, 9, 101, 109, 112, 122, 189]
    list_b = [0, 2, 4, 5, 6, 8, 10, 100]
    s_obj = Solution()
    s_obj.merge(list_a, list_b)
    print list_a
