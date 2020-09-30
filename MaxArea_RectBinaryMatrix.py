def solve_nsr(A):
    s = []
    nsr = []
    n = len(A)
    # s.append((A[n-1], 0))
    for i in range(n-1, -1, -1):
        if(len(s) == 0):
            nsr.append(-1)
        elif(len(s) > 0 and s[-1][0] < A[i]):
            nsr.append(s[-1][1])
        elif(len(s) > 0 and s[-1][0] >= A[i]):
            while(len(s) > 0 and s[-1][0] >= A[i]):
                s.pop()
            if(len(s) == 0):
                nsr.append(n)
            else:
                nsr.append(s[-1][1])
        s.append((A[i], i))

    return nsr[::-1]

def solve_nsl(A):
    s = []
    nsl = []
    # s.append((A[0], 0))
    n = len(A)
    for i in range(n):
        if(len(s) == 0):
            nsl.append(-1)
        elif(len(s) > 0 and s[-1][0] < A[i]):
            nsl.append(s[-1][1])
        elif(len(s) > 0 and s[-1][0] >= A[i]):
            while(len(s) > 0 and s[-1][0] >= A[i]):
                s.pop()
            if(len(s) == 0):
                nsl.append(-1)
            else:
                nsl.append(s[-1][1])
        s.append((A[i], i))

    return nsl

def Mah(A):
    n = len(A)
    # width = []
    nsr = solve_nsr(A)
    nsl = solve_nsl(A)
    width = [nsr[i] - nsl[i] - 1 for i in range(n)]
    Area = [width[i] * A[i] for i in range(n)]
    
    return max(Area)


def Binary(A, m , n):
    l = len(A)
    v = []
    for i in range(n): 
        v.append(A[0][i])

    mx = Mah(v)
    for i in range(1, m):
        for j in range(0, n):
            if(A[i][j] == 0):
                v[j] = 0
            else:
                v[j] = v[j] + A[i][j]
        mx = max(mx, Mah(v))
    # print(v)
    return mx


A = [[0, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 0]]
m = len(A)
n = len(A[0])
# print(m, n)
x = Binary(A, m, n)
print(x) 