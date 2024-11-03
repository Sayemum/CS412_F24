"""
    name: Sayemum Hassan

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.

           Comments here on your code and submission.
"""


from queue import PriorityQueue

def InitSSSP(verticesNum):
    graph = []
    
    for i in range(verticesNum):
        graph.append([i, float('inf'), None])
    graph[0][1] = 0
    
    return graph


def Dijkstras(verticesNum, edges, source):
    graph = InitSSSP(verticesNum)
    pq = PriorityQueue()
    pq.put((0, source))
    
    while not pq.empty():
        u = pq.get()
        
        if u[0] > graph[u[1]][1]:
            continue
        
        for edge in edges:
            if u[1] == edge[0]:
                # if tense edge
                if u[0] + edge[2] < graph[edge[1]][1]:
                    # relax edge
                    graph[edge[1]][1] = u[0] + edge[2]
                    graph[edge[1]][2] = u[1]
                    pq.put((graph[edge[1]][1], edge[1]))
    
    return graph


def Report_Query(graph, query):
    result = graph[query[1]][1]
    return result if result != float('inf') else "Impossible"


def main():
    # example input
    # verticesNum = 4
    # edgesNum = 3
    # queriesNum = 4
    # edges = [(0, 1, 2), (1, 2, 2), (3, 0, 2)]
    # queries = [(0, 0), (0, 1), (0, 2), (0, 3)]
    
    
    # get input
    
    given = input().split()
    edges = []
    queries = []
    
    verticesNum = int(given[0])
    edgesNum = int(given[1])
    queriesNum = int(given[2])
    
    for _ in range(edgesNum):
        edgeStr = input().split()
        edges.append((int(edgeStr[0]), int(edgeStr[1]), int(edgeStr[2])))
    
    for _ in range(queriesNum):
        queryStr = input().split()
        queries.append((int(queryStr[0]), int(queryStr[1])))
    
    # Output
    for query in queries:
        graph = Dijkstras(verticesNum, edges, query[0])
        print(Report_Query(graph, query))


if __name__ == "__main__":
    main()
