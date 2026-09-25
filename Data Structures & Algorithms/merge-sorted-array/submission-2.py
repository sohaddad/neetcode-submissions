class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m] = nums2[i]
            j = m - 1
            m += 1
            while j >= 0 and nums1[j + 1] < nums1[j]:
                # arr[j] and arr[j + 1] are out of order so swap them 
                tmp = nums1[j + 1]
                nums1[j + 1] = nums1[j]
                nums1[j] = tmp
                j -= 1
        return nums1

        