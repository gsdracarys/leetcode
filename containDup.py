def containsDuplicate(nums: list) -> bool:
    nums.sort()
    if len(nums) > 1:
        for i in range(len(nums)):
            if nums[i-1] == nums[i]:
                print("true")
                return True
    else:
        return False
        print("false")
            
containsDuplicate([1,2,2,1])