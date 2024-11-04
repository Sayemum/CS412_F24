"""
    name: Sayemum Hassan

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.

           Comments here on your code and submission.
"""

import math


def arbitrage(num_rates, exchanges):
    pass
    # detect if product of all exchanges is greater than 1

def create_graph(exchanges):
    graph = []
    
    for exchange in exchanges:
        graph.append([exchange[0], exchange[1], -math.log(exchange[2])])
    
    return graph

def InitSSSP(verticesNum):
    graph = []
    
    for i in range(verticesNum):
        graph.append([i, float('inf'), None])
    graph[0][1] = 0
    
    return graph

def Bellman_Ford(num_rates, exchanges):
    graph = InitSSSP(num_rates)
    
    # relax edges v - 1 times
    for _ in range(num_rates - 1):
        for exchange in exchanges:
            print(exchange)
    
    return graph

def main():
    # example input
    num_rates = 4
    exchanges = [('USD', 'EUR', 0.82), ('EUR', 'JPY', 129.7), ('JPY', 'TRY', 12.0), ('TRY', 'USD', 0.0008)]
    
    # get input
    # num_rates = int(input())
    # exchanges = []
    
    # for _ in range(num_rates):
    #     exchange = input().split()
    #     exchanges.append((exchange[0], exchange[1], float(exchange[2])))
    
    print(exchanges)
    graph = create_graph(exchanges)
    print(graph)
    bellman = Bellman_Ford(num_rates, exchanges)

if __name__ == "__main__":
    main()
