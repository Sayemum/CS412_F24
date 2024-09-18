def is_palindrome(s):
    return s == s[::-1]


def palincount(s):
    cache = []
    def inner_function(startIdx):
        # if s in cache:
        if startIdx in cache:
            # return cache[s]
            return cache[startIdx]
        if len(s) == 1 or len(s) == 0:
            return 1
        
        # exhausavely draw the first line and figure out what works
        count_subpartitions = 0
        
        for idx in range(1, len(s) + 1):
            if is_palindrome(s[:idx]):
                # count_subpartitions += inner_function(s[idx:])
                count_subpartitions += inner_function(startIdx + 1)
        
        # cache[s] = count_subpartitions
        cache.append(count_subpartitions)
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
