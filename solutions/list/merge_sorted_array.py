# 88. Merge Sorted Array

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # nums1 = nums1[0:m]
        print(nums1)
        if len(nums1) == 0:
            return nums2
        if len(nums2) == 0:
            return nums1
        i1 = m - 1
        i2 = n - 1
        i = m + n - 1
        while i2 >= 0 and i1 >= 0:
            n2 = nums2[i2]
            n1 = nums1[i1]
            print([i1, i2, n1, n2])
            print(["nums1", nums1])

            if n2 <= n1:
                nums1[i] = n1
                print(["insert", n1])
                # nums1.insert(i1, n2)
                i1 -= 1
            else:
                print(["append", n2])
                nums1[i] = n2
                i2 -= 1

            i -= 1
        
        while i2 >= 0:
            n2 = nums2[i2]
            nums1[i] = n2
            i2 -= 1 
            i -= 1  

        while i1 >= 0:
            n1 = nums1[i1]
            nums1[i] = n1
            i1 -= 1 
            i -= 1  

        # print(["final:", nums1])
        # return nums1

