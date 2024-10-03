"""
    name:  Sayemum Hassan

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.

           Comments here on your code and submission.
"""


def knapsack(i, w):
    pass


def main():
    # get input
    # n = 3
    # remove_coords = (0, 0)
    # section_lengths = list(map(int, input().split()))
    # height = int(input())
    
    weight = int(input())
    n = int(input())
    
    triples = []
    for _ in range(n):
        line = input().split()
        triples.append((line[0], float(line[1]), float(line[2])))

    print(triples)

if __name__ == "__main__":
    main()
