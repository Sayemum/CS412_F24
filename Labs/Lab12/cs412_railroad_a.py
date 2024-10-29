"""
    name: Sayemum Hassan

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.

           Comments here on your code and submission.
"""

from connected_components import count_and_label
import math


def add_all_safe_edges(graph, mst, comp, comp_count):
    safe = [None] * comp_count
    
    for u in graph:
        for v in graph[u]:
            if comp[u] != comp[v]:
                weight = graph[u][v]
                
                # Check if we have a better edge for u
                if safe[comp[u]] is None or weight < safe[comp[u]][1]:
                    safe[comp[u]] = (v, weight)

                # Check if we have a better edge for v
                if safe[comp[v]] is None or weight < safe[comp[v]][1]:
                    safe[comp[v]] = (u, weight)
    
    
    # Add the selected edges to mst
    for u in range(comp_count):
        if safe[u] is not None:
            v, weight = safe[u]
            
            mst[u][v] = weight
            mst[v][u] = weight


def boruvka(graph):
    mst = { i:{} for i in range(len(graph)) }
    
    comp_count, comp = count_and_label(mst)
    
    while comp_count > 1:
        add_all_safe_edges(graph, mst, comp, comp_count)
        comp_count, comp = count_and_label(mst)
        
    return mst


def main():
    # get input
    
    n = int(input())
    
    # # create adjascency list of all vertices with their adj edges (empty dict)
    graph = {}
    coords = {}
    for i in range(n):
        line = input().split()
        x, y = float(line[0]), float(line[1])
        
        graph[i] = {}
        coords[i] = (x, y)
    
    # Populate adj list with edges & weights
    for i in range(n):
        for j in range(i+1, n):
            x1,y1 = coords[i]
            x2,y2 = coords[j]
            
            # euclidean distance
            dist = math.sqrt( math.pow(x2-x1, 2) + math.pow(y2-y1, 2) )
            
            # undirected graph, so apply two edges
            graph[i][j] = dist
            graph[j][i] = dist
    
    mst = boruvka(graph)
    
    # calculate total cost and print
    total_weight = 0.0
    
    for u in mst:
        for v in mst[u]:
            if u < v:
                total_weight += mst[u][v]

    total_cost = total_weight * 1_000_000
    
    print(f"${total_cost / 1_000_000:.1f}M")


if __name__ == "__main__":
    main()
