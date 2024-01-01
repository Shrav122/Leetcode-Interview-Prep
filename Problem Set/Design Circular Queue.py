# Time Complexity: O(1)
# Space Complexity: O(N)
class MyCircularQueue:

    def __init__(self, k: int):
        # the queue holding the elements for the circular queue
        self.q = [0] * k
        # the number of elements in the circular queue
        self.cnt = 0
        # queue size
        self.sz = k
        # the idx of the head element
        self.headIdx = 0
        

    def enQueue(self, value: int) -> bool:
        # handle full case
        if self.isFull(): return False
        self.q[(self.headIdx + self.cnt) % self.sz] = value
        # increase the number of elements by 1
        self.cnt += 1
        return True

    def deQueue(self) -> bool:
        # handle empty case
        if self.isEmpty(): return False
        # update the head index
        self.headIdx = (self.headIdx + 1) % self.sz
        # decrease the number of elements by 1
        self.cnt -= 1
        return True

    def Front(self) -> int:
        # handle empty queue case
        if self.isEmpty(): return -1
        # return the head element
        return self.q[self.headIdx]
        
    def Rear(self) -> int:
        # handle empty queue case
        if self.isEmpty(): return -1
        return self.q[(self.headIdx + self.cnt - 1) % self.sz]

    def isEmpty(self) -> bool:
        # no element in the queue
        return self.cnt == 0

    def isFull(self) -> bool:
        # return True if the count is equal to the queue size
        # else return False
        return self.cnt == self.sz