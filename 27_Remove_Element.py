class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize two pointers: 
        # `start` points to the beginning of the array
        # `end` points to the last element of the array
        start = 0
        end = len(nums) - 1
        
        # Loop until the `start` pointer crosses the `end` pointer
        while(start <= end):
            # If the element at `start` is equal to `val`, we need to remove it
            if nums[start] == val:
                # If the element at `end` is also `val`, just move `end` left
                if nums[end] == val:
                    end = end - 1
                    continue
                
                # If `nums[start]` is `val`, but `nums[end]` is not `val`, swap them
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                
                # After swapping, move `end` left as we've moved a non-`val` element to the end
                end = end - 1
            # Move `start` to the right, as we've processed the current element
            start = start + 1
        
        # The new length of the array is the position of `end` + 1
        return end + 1

    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize the pointer `i` to traverse through the array
        # `index_to_update` will track where the next non-`val` element should be placed
        i = 0
        index_to_update = 0
        length = len(nums)
        
        # Loop through the array
        while(i < length):
            # If the current element is not `val`, move it to the front
            if nums[i] != val:
                # Place the current element at `index_to_update`
                nums[index_to_update] = nums[i]
                # Increment `index_to_update` as we have placed a valid element
                index_to_update += 1
            # Move to the next element
            i += 1
        
        # The new length is the number of elements that are not `val`
        return index_to_update



                


        