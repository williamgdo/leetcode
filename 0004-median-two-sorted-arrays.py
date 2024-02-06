from typing import List


class Solution:
    def mergeArrays(self, arr_a: List[int], arr_b: List[int]) -> List[int]:
        arr_a_len = len(arr_a)
        arr_b_len = len(arr_b)
        arr_c_len = arr_a_len + arr_b_len

        index_a, index_b = 0, 0
        nums3 = []

        if arr_a_len == 0 and arr_b_len == 0:
            return []

        while index_a < arr_a_len and index_b < arr_b_len:
            if arr_a[index_a] < arr_b[index_b]:
                nums3.append(arr_a[index_a])
                index_a += 1
            else:
                nums3.append(arr_b[index_b])
                index_b += 1

        while index_a < arr_a_len:
            nums3.append(arr_a[index_a])
            index_a += 1

        while index_b < arr_b_len:
            nums3.append(arr_b[index_b])
            index_b += 1

        return nums3

    def getMedian(self, array: List[int]):
        length = len(array)
        mid = length // 2
        if length % 2 == 0:
            return (array[mid] + array[mid - 1]) / 2
        else:
            return array[mid]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0 and len(nums2) == 0:
            return 0

        nums3 = self.mergeArrays(nums1, nums2)
        return self.getMedian(nums3)
