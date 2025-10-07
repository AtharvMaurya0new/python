class Solution(object):
    def removeElement(self, nums, val):
        y=[]
        i=0
        while i<len(nums):
            if nums[i]!=val:
                 y.append(nums[i])
            i+=1    
        return y   

# Main function
if __name__ == "__main__":
    # Create object of Solution
    obj = Solution()

    # Example input
    nums = [3, 2, 2,3]
    val = 3

    # Call the method
    result = obj.removeElement(nums, val)

    # Print result
    print("Original list:", nums)
    print("Value to remove:", val)
    print("Resulting list:", result)
