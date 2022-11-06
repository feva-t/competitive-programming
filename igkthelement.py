class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k, self.minHeap = k, nums
        heapq.heapify(self.minHeap)

        print(f" heapq = {self.minHeap},{nums}")
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
    def add(self, v: int) -> int:
        heapq.heappush(self.minHeap, v) 
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
    # self.__init__()

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
  2  
oct20- nov 01 (2022)/heap sort| geeksforgeeks .py
@@ -7,7 +7,7 @@ def heapify(self,arr, n, i):
            mx = r
        if (l < n and arr[l] > arr[mx] ):
            mx = l

                                                                            
        if (i != mx):
            arr[mx], arr[i] = arr[i], arr[mx]
            self.heapify(arr, n, mx)
