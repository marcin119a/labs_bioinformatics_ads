def Partition(A, l, r):
    i = l+1
    j = r-1
    while True:
        while i < r and A[i] <= A[l]: i += 1
        while A[j] > A[l]: j -= 1
        if i < j:
            (A[i], A[j]) = (A[j], A[i])
        else:
            break
        (A[l], A[j]) = (A[j], A[l])
    return A[j]

print(Partition([3, 1, 2, 5, 3, 4, 1], 0, 7))
print(Partition([7, 1, 2, 5, 4, 2, 1], 2, 6))
print(Partition([1, 2, 3, 4, 5, 6, 7], 0, 7))