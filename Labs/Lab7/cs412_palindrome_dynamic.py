"""
ANALYSIS:
O(1) - lines 16,17
O(n) - lines 19,21,22
The outer i loop is O(n) while the inner j loop has each i+1 going to n.
A palindrome check is called O(n^2) in worst case and each item takes O(n).
So the runtime is O(n^3).
"""


def is_palindrome(s):
    return s == s[::-1]


def palincount(s):
    cache = [0] * (len(s) + 1) 
    cache[len(s)] = 1
    
    for i in range(len(s)-1, -1 ,-1):
        total = 0
        for j in range(i + 1, len(s) + 1):
            if is_palindrome(s[i:j]):
                total += cache[j]
        cache[i] = total
    
    return cache[0]


def main():

    n = int(input())

    # get lines of input
    lines = []
    
    # n = 1
    # lines = ["abc"]
    
    for _ in range(n):
        lines.append(input())
    
    for s in lines:
        print(palincount(s))


if __name__ == "__main__":
    main()
