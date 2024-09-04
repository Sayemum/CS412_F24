"""
   MergeSort
   coded by Bowers from Jeff Erickson's pseudocode
"""


def mergesort(A, inversions):
    if len(A) > 1:
        # Get the mid point
        m = len(A) // 2

        # Get the left and right halves
        left, right = A[:m], A[m:]

        # sort the left and right halves
        mergesort(left, inversions)
        mergesort(right, inversions)

        # Copy the sorted left and right halves back to A. 
        for i in range(m):
            A[i] = left[i]
        for j in range(m, len(A)):
            A[j] = right[j - m]
        
        # Run the merge operation on A
        merge(A, m, inversions)


def merge(A, m, inversions):
    i, j = 0, m
    n = len(A)
    B = [0 for _ in range(n)]
    for k in range(n):
        if j >= n:
            B[k] = A[i]
            i += 1
        elif i >= m:
            B[k] = A[j]
            j += 1
        elif A[i] <= A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
            inversions[0] += m - i  # Count inversions
    for k in range(n):
        A[k] = B[k]


def main():
    A = list(map(int, input().split()))
    inversions = [0]
    
    mergesort(A, inversions)
    
    # print("List:", A)
    # print("Number of Inversions:", inversions[0])
    print(inversions[0])


if __name__ == "__main__":
    main()
