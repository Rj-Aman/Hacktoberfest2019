class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        num_set = set()
        mx = -1
        for i in range(len(A)):
            if A[i] in num_set:
                return A[i]
            else:
                num_set.add(A[i])
        return -1
            

if __name__ == "__main__":
    A = [3, 1, 4, 5]
    sol = Solution()
    s = sol.repeatedNumber(A)
    print(s)