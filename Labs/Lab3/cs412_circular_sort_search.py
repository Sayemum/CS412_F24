def circ_search(A, start_idx, end_idx, search_key):
    # BASE CASES
    if end_idx < start_idx:
        return -1
    if start_idx == end_idx:
        if A[start_idx] == search_key:
            return start_idx
        else:
            return -1
    
    mid_point = (start_idx + end_idx) // 2
    if A[mid_point] == search_key:
        return mid_point

    # RECURSIVE
    if A[mid_point + 1] <= A[end_idx]: # right side sorted
        if A[mid_point + 1] <= search_key <= A[end_idx]:
            return circ_search(A, mid_point+1, end_idx, search_key) # recurse right side
        else:
            return circ_search(A, start_idx, mid_point-1, search_key) # recurse left side
    else: # left side sorted
        if A[start_idx] <= search_key <= A[mid_point - 1]:
            return circ_search(A, start_idx, mid_point-1, search_key) # recurse left side
        else:
            return circ_search(A, mid_point+1, end_idx, search_key) # recurse right side


def main():
    """NOTES/APPROACH:
    1. Understand the examples
    2. What are we studying right now? (Recursion and Divide & Conquer)
    3. What are the constraints? (O(lg n))
    """

    in_list = list(map(int, input().split()))
    search_item = int(input())

    print(in_list)
    print(search_item)
    
    print(circ_search(in_list, 0, len(in_list)-1, search_item))



if __name__ == "__main__":
    main()
