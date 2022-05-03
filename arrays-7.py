# https://practice.geeksforgeeks.org/problems/chocolate-distribution-problem3825/
def findMinDiff(self, A,N,M):

        # code here
        ans = []
        A.sort()
        for idx in range(N-M+1):
            ans.append(A[idx+M-1]-A[idx])
        return min(ans)
