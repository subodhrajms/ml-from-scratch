def matmul(A, B):
  m = len(A)
  n = len(A[0])
  p = len(B[0])

  #creating a result matrix of zeros
  C = [[0.0 for _ in range(p)] for _ in range(m)]

  #multiplication logic
  for i in range(m):
    for j in range(p):
      for k in range(n):
        C[i][j] += A[i][k]*B[k][j]

  return C
