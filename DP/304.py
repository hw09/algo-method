N = int(input())
A = [1, 1]
for i in range(2, N+1):
    A.append(A[i-1] + A[i-2])
print(A[N])