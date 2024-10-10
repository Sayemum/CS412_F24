"""
    name: Sayemum Hassan

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.

           Comments here on your code and submission.
"""


def search(stack, stops_connected, startV, endV):
    stack.append(startV)
    visited = set()
    correct_path = []
    
    while stack:
        v = stack.pop()
        
        if v not in visited:
            visited.add(v)
            correct_path.append(v)
            
            for w in stops_connected[v]:
                if w not in visited:
                    stack.append(w)
        
        if v == endV:
            return correct_path

    return -1


def main():
    # get input
    
    n = int(input())
    
    # Key is each stop as string and value is a list of all connected stops
    stops_connected = {}
    for _ in range(n):
        line = input().split()
        stop1, stop2 = line[0], line[1]
        
        if stops_connected.get(stop1) == None:
            stops_connected[stop1] = []
            stops_connected[stop1].append(stop2)
        else:
            stops_connected[stop1].append(stop2)
        
        if stops_connected.get(stop2) == None:
            stops_connected[stop2] = []
            stops_connected[stop2].append(stop1)
        else:
            stops_connected[stop2].append(stop1)
    
    query = input().split()
    stack = []
    correct_path = search(stack, stops_connected, query[0], query[1])
    
    if correct_path == -1:
        print("no route possible")
    else:
        print(" ".join(correct_path))
    

if __name__ == "__main__":
    main()
