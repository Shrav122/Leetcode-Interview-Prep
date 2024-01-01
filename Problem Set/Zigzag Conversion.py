class Solution(object):
    def convert(self, s, numRows):
        if numRows <= 1:
            return s

        v = [""] * numRows
        j, dir = 0, -1

        for i in range(len(s)):
            if j == numRows - 1 or j == 0:
                dir *= -1

            v[j] += s[i]

            if dir == 1:
                j += 1
            else:
                j -= 1

        res = "".join(v)
        return res

        
        