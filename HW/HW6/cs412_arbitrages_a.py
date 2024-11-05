"""
    name: Sayemum Hassan

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.

           Comments here on your code and submission.
"""

import math


def InitSSSP(given, source):
    graph = {}
    
    for u in given:
        graph[u] = [float('inf'), None]
    graph[source] = [0, None]
    
    return graph


def Bellman_Ford(graph, source):
    table = InitSSSP(graph, source)
    
    for _ in range(len(graph)-1):
        for u in graph:
            for v in graph[u]:
                if (table[u][0] + math.log(graph[u][v], 10) < table[v][0]):
                    table[v][0] = table[u][0] + math.log(graph[u][v], 10)
                    table[v][1] = u
    
    return table


def detect_arbitrage(exchanges, source):
    table = Bellman_Ford(exchanges, source)
    
    for u in exchanges:
        for v in exchanges[u]:
            if v != source:
                continue
            
            if table[u][0] + math.log(exchanges[u][v], 10) > 0:
                # create path
                path = [source]
                parent = u
                
                while parent is not None:
                    path.append(parent)
                    parent = table[parent][1]
                path.reverse()
                
                # check if cycle made net gain
                negative_cycle_total = 0
                for i in range(len(path)-1):
                    negative_cycle_total += -math.log(exchanges[path[i]][path[i+1]], 10)
                
                if negative_cycle_total < 0:
                    factor_increase = 10 ** (-negative_cycle_total)
                    return True, path, factor_increase
    
    return False, [], 0


def main():
    # get input
    num_rates = int(input())
    exchanges = {}
    
    for _ in range(num_rates):
        exchange = input().split()
        exchanges[exchange[0]] = {exchange[1]: float(exchange[2])}
    
    detected, path, factor_increase = detect_arbitrage(exchanges, list(exchanges.keys())[0])
    
    if detected:
        print("Arbitrage Detected")
        
        for i in range(len(path)-1):
            print(f"{path[i]} => ", end="")
        print(path[-1])
        
        print(f"{factor_increase:.5f} factor increase")
    else:
        print("No Arbitrage Detected")


if __name__ == "__main__":
    main()
