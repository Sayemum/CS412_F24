def is_palindrome(s):
    return s == s[::-1]


def palincount(s):
    cache = {}
    
    def inner_function(s):
        if s in cache:
            return cache[s]
        if len(s) == 1 or len(s) == 0:
            return 1
        
        # exhausavely draw the first line and figure out what works
        count_subpartitions = 0
        
        for idx in range(1, len(s) + 1):
            if is_palindrome(s[:idx]):
                count_subpartitions += inner_function(s[idx:])
        
        cache[s] = count_subpartitions
        return count_subpartitions
        
    return inner_function(s)


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
