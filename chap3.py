def binary_search(A,x):
    p, r, i  = 0, len(A), 1
    while p<=r:
        # print "Iteration %d" % (i)
        # i += 1
        q = (p+r) / 2
        if A[q] == x:
            return q
        elif A[q] < x:
            p = q+1
        elif A[q] > x:
            r = q-1
    return -1
    

def selection_sort(A):
    iterations = 0
    for i in range(0, len(A)):
        smallest = i
        for j in range(i, len(A)):
            iterations += 1
            if A[j] < A[smallest]:
                smallest = j
        A[i], A[smallest] = A[smallest], A[i]
    # print "Iterations = %d, n = %d" % (iterations, len(A))
    return A
    
    

