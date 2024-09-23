def is_palindrome(s):
    return s == s[::-1]


def palincount(s):
    cache = [None] * (len(s) + 1) 
    cache[len(s)] = 1
    
    def inner_function(i):
        if cache[i] is not None:
            return cache[i]

        total = 0
        for j in range(i, len(s)):
            if is_palindrome(s[i:j+1]):
                total += inner_function(j-1)

        cache[i] = total
        return total

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
