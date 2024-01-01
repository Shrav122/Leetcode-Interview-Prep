#Not a Leetcode Problem
def rotateMatrix(self, data):
 
    rows = len(data)
    cols = len(data[0])
    # Reversing all rows
    for i in range(len(data)):
        data[i] = data[i][::-1]
    # Reversing all rows of the matrix
    data = data[::-1]
    for i in range(rows):
        for j in range(cols):
            print(data[i][j], end=' ')
        print()