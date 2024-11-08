"""
CS 412 Lab: Maxflow and Min cut

Name: Sayemum Hassan

Implement the Ford/Fulkerson augmenting-path algorithm for computing the
max flow of a graph. 
"""


import queue
import sys


"""
Depth first search

Accepts a graph in an adjacency list (does not care about payload for edges)
Starts a traversal at s and stops when either there are no more vertices
to explore or it reaches vertex t.

Returns: list of predecesors/parents in the tree resulting from the DFS.
If vertex t is unreachable, it will not be in the returned dictionary
"""
def dfs(G, s, t):
    bag = queue.LifoQueue()
    bag.put((None, s))
    dfs_parents = {}
    while not bag.empty() and dfs_parents.get(t) is None:

        p, u = bag.get()

        if u not in dfs_parents:
            dfs_parents[u] = p 
            for v in G[u]:
                bag.put((u,v))

    return dfs_parents            


def build_res(G):
    residual = {}
    for u in G:
        residual[u] = {}
    
    for u in G:
        for v in G[u]:
            flow, cap = G[u][v]
            if cap != flow:
                residual[u][v] = cap - flow
            if flow != 0:
                residual[v][u] = flow
    
    return residual


def extract_path(spanning_tree, t):
    path = [t]
    current_node = t
    
    while spanning_tree[current_node] is not None:
        path.append(spanning_tree[current_node])
        current_node = spanning_tree[current_node]
    
    path.reverse()
    return path


def maxflow(G, s, t):
    while True:
        G_res = build_res(G) 
        spanning_tree = dfs(G_res, s, t) # p = findAugmentingPath()
        
        if t not in spanning_tree:
            break
        
        path = extract_path(spanning_tree, t)
        
        print(G_res)
        print(spanning_tree)
        print(path)
        sys.exit(0)
        
        adj_flows(G, path)


def main():
    # example
    vertex_count = 6
    edge_count = 9
    adj_list = {0: {1: [0, 20], 2: [0, 10]}, 1: {2: [0, 10], 3: [0, 5]}, 2: {4: [0, 10]}, 3: {2: [0, 15], 5: [0, 15]}, 4: {3: [0, 10], 5: [0, 20]}, 5: {}}

    # vertex_count, edge_count = [int(x) for x in input().split()]

    # adj_list = {}
    # # create vertices numbered 0 to vertex_count - 1
    # for i in range(vertex_count):
    #     adj_list[i] = {}

    # # the value for each edge is a list.  First element is the flow, 
    # # second element is the capacity.

    # for _ in range(edge_count):
    #     u, v, cap = [int(x) for x in input().split()]
    #     adj_list[u][v]= [0, cap]

    # print('adjlist', adj_list)
    # sys.exit(0)

    # by the problem definition, define s and t as follows
    s = 0    
    t = vertex_count - 1
    
    maxflow(adj_list, s, t)
    

if __name__ == "__main__":
    main()
