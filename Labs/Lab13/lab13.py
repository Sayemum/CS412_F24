"""
    name: Sayemum Hassan

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.

           Comments here on your code and submission.
"""


def main():
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
    
    print(verticesNum)
    print(edges)
    print(queries)
    # InitSSSP(verticesNum, edges)
    Dijkstras(verticesNum)


def InitSSSP(verticesNum):
    graph = []
    
    for i in range(verticesNum):
        graph.append([i, float('inf'), None])
    graph[0][1] = 0
    
    return graph
    

def Dijkstras(verticesNum, edges):
    graph = InitSSSP(verticesNum)
    


if __name__ == "__main__":
    main()
