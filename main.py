class MyClass:
    def __init__(self, nums: list) -> None:
        self.nums = nums
        self.size = len(nums)

    def getLength(self):
        return self.size
    
print(MyClass([1,2,3]).getLength())