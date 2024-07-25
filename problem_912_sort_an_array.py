from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, lf, mid, rg):

            res = []
            i = lf
            j = mid
            while i < mid and j < rg:
                if arr[i] < arr[j]:
                    res.append(arr[i])
                    i += 1
                else:
                    res.append(arr[j])
                    j += 1
            while i < mid:
                res.append(arr[i])
                i += 1
            while j < rg:
                res.append(arr[j])
                j += 1
            return res

        def merge_sort(arr, lf, rg):
            if rg - lf <= 1:
                return
            mid = (lf + rg) // 2
            merge_sort(arr, lf, mid)
            merge_sort(arr, mid, rg)
            res = merge(arr, lf, mid, rg)
            arr[lf:rg] = res

        merge_sort(nums, 0, len(nums))
        return nums
