def is_palindrome(s):
    return s == s[::-1]


def palincount(s):
    cache = [-1] * (len(s) + 1) 
    
    def inner_function(startIdx):
        if cache[startIdx] != -1:
            return cache[startIdx]
        if startIdx >= len(s):
            return 1

        count_subpartitions = 0

        for idx in range(startIdx + 1, len(s) + 1):
            if is_palindrome(s[startIdx:idx]):
                count_subpartitions += inner_function(idx)

        cache[startIdx] = count_subpartitions
        return count_subpartitions

    return inner_function(0)


def main():

    n = int(input())

    # get lines of input
    lines = []
    
    for _ in range(n):
        lines.append(input())
    
    for s in lines:
        print(palincount(s))


if __name__ == "__main__":
    main()
