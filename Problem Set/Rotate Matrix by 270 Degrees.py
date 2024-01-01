#Not a Leetcode Problem
def rotateMatrix(data: List[int][int]) -> List[int][int]:
    for i in range(n):
        for j in range(n):
            self.swap(data[i][j], data[j][i])
    for i in range(n/2):
        self.swap(data[i], data[n-i-1])
    return data

def swap(self, x, y):
    temp = x
    x = y
    y = temp