"""
    name: Sayemum Hassan

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.

           Comments here on your code and submission.
"""


def main():
    # get input
    
    n = int(input())
    
    graph = {}
    for _ in range(n):
        line = input().split()
        x, y = line[0], line[1]
        coord = (x, y)
        
        if graph.get(coord) == None:
            graph[coord] = 0
    
    print(graph)
    

if __name__ == "__main__":
    main()
