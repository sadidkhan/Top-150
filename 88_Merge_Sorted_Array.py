class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return;
        
        last_index = len(nums1) - 1

        # Merge in reverse order
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last_index] = nums1[m-1]
                m = m - 1
            else:
                nums1[last_index] = nums2[n-1]
                n = n - 1

            last_index -= 1
        
        #fills nums1 with leftover elements of nums2 [Case m=0 nums1 = [0], n=1, nums2= [1]]
        while n>0:
            nums1[last_index] = nums2[n-1]
            n = n-1
            last_index -= 1


        
        