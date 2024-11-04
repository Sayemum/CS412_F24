"""
    name: Sayemum Hassan

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.

           Comments here on your code and submission.
"""


def main():
    # example input
    # verticesNum = 4
    # edgesNum = 3
    # queriesNum = 4
    # edges = [(0, 1, 2), (1, 2, 2), (3, 0, 2)]
    # queries = [(0, 0), (0, 1), (0, 2), (0, 3)]
    
    
    # get input
    
    num_rates = int(input())
    exchanges = []
    
    for _ in range(num_rates):
        exchange = input().split()
        exchanges.append((exchange[0], exchange[1], float(exchange[2])))
    
    print(exchanges)

if __name__ == "__main__":
    main()
