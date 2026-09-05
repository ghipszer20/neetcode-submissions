class MedianFinder:

    def __init__(self):
        self.arr = []
        self.size = 0
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()
        
        self.size += 1


    def findMedian(self) -> float:
        if self.size == 0:
            return
        elif self.size % 2 == 1:
            return self.arr[self.size // 2]

        mid = self.size // 2
        return (self.arr[mid] + self.arr[mid - 1]) / 2
        
        