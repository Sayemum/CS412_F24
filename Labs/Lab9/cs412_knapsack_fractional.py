"""
    name:  Sayemum Hassan

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.

           Comments here on your code and submission.
"""


def frac_knapsack(i, w):
    pass


def main():
    # get input
    # n = 3
    # remove_coords = (0, 0)
    # section_lengths = list(map(int, input().split()))
    # height = int(input())
    
    w = int(input())
    n = int(input())
    
    triples = []
    for _ in range(n):
        line = input().split()
        # triples.append((line[0], float(line[1]), float(line[2])))
        triples.append([line[0], float(line[1]), float(line[2])])

    # print(triples)
    
    triples.sort(key=lambda x: (x[1] / x[2]), reverse=True)
    
    # print(triples)
    
    total = 0.0
    
    for item in triples:
        if item[2] <= w:
            w -= item[2]
            total += item[1]
        else:
            total += item[1] * w / item[2]
            break
    
    # print(triples)
    for item in triples:
        print(f"{item[0]}({item[1]:.2f}, {item[2]:.2f})", end=" ")
    
    print()
    print(total)

if __name__ == "__main__":
    main()
