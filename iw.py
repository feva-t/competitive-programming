from sortedcontainers import SortedList

class MedianFinder:
    def __init__(self):
        self.nums = SortedList()

    def addNum(self, num: int) -> None:
        self.nums.add(num)

    def findMedian(self) -> float:
        l = len(self.nums)
        if l % 2:
            return self.nums[l // 2]
        return (self.nums[(l - 1) // 2] + self.nums[l // 2]) / 2
    
    
# # Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
