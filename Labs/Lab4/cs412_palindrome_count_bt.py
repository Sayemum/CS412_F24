def is_palindrome(s):
    return s == s[::-1]


def recurse(s):
    if len(s) == 1 or len(s) == 0:
        return 1
    
    # exhausavely draw the first line and figure out what works
    total = 0
    
    for idx in range(1, len(s) + 1):
        if is_palindrome(s[:idx]):
            total += recurse(s[idx:])
    
    return total


def main():

    # n = int(input())
    # lines = list(input().split())
    n = 3
    lines = ["abc", "bcccb", "seeks"]

    # print(n)
    # print(lines)
    
    for s in lines:
        print(recurse(s))
    
    # print(circ_search(in_list, 0, len(in_list)-1, search_item))


if __name__ == "__main__":
    main()
