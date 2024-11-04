import math

def detect_arbitrage(num_exchanges, exchange_data):
    # Build the graph
    graph = {}
    currencies = set()
    for (cIn, cOut, rate) in exchange_data:
        if cIn not in graph:
            graph[cIn] = []
        graph[cIn].append((cOut, -math.log(rate)))
        currencies.update([cIn, cOut])
    
    # Initialize distances and predecessors
    distances = {currency: float('inf') for currency in currencies}
    predecessors = {currency: None for currency in currencies}
    
    # Pick an arbitrary start node (any node will do, we just need to start somewhere)
    start_currency = list(graph.keys())[0]
    distances[start_currency] = 0
    
    # Relax edges up to |V| - 1 times
    for _ in range(len(currencies) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    predecessors[v] = u
    
    # Check for negative weight cycles
    for u in graph:
        for v, weight in graph[u]:
            if distances[u] + weight < distances[v]:
                # Negative cycle detected
                # To find the cycle, we trace predecessors
                arbitrage_cycle = []
                arbitrage_currencies = set()
                current = v
                
                # Find a cycle starting point
                for _ in range(len(currencies)):
                    current = predecessors[current]
                
                # Trace the cycle
                cycle_start = current
                while True:
                    if current in arbitrage_currencies:
                        cycle_start = current
                        break
                    arbitrage_cycle.append(current)
                    arbitrage_currencies.add(current)
                    current = predecessors[current]
                
                # Collect the cycle starting from the detected cycle_start
                arbitrage_cycle = []
                current = cycle_start
                while True:
                    arbitrage_cycle.append(current)
                    current = predecessors[current]
                    if current == cycle_start:
                        arbitrage_cycle.append(current)
                        break
                
                arbitrage_cycle.reverse()
                
                # Calculate the product of the exchange rates in the cycle
                product = 1.0
                for i in range(len(arbitrage_cycle) - 1):
                    u = arbitrage_cycle[i]
                    v = arbitrage_cycle[i + 1]
                    for (cIn, cOut, rate) in exchange_data:
                        if u == cIn and v == cOut:
                            product *= rate
                            break
                
                # Output the arbitrage detection and the cycle
                print("Arbitrage Detected")
                print(" => ".join(arbitrage_cycle))
                print(f"{product:.5f} factor increase")
                return
    
    print("No Arbitrage Detected")

# Sample input processing
num_exchanges = 4
exchange_data = [
    ("USD", "EUR", 0.82),
    ("EUR", "JPY", 129.7),
    ("JPY", "TRY", 12),
    ("TRY", "USD", 0.0008)
]

detect_arbitrage(num_exchanges, exchange_data)
