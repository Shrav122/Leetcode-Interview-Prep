    def diagonalSort(self, A):
        n, m = len(A), len(A[0])
        d = collections.defaultdict(list)
        for i in xrange(n):
            for j in xrange(m):
                d[i - j].append(A[i][j])
        for k in d:
            d[k].sort(reverse=1)
        for i in xrange(n):
            for j in xrange(m):
                A[i][j] = d[i - j].pop()
        return A