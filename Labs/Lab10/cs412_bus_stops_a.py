"""
    name: Sayemum Hassan

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.

           Comments here on your code and submission.
"""


def search(stack, stops_connected, startV, endV):
    stack.append(startV)
    stops = list(stops_connected.keys())
    correct_path = []
    # print(type(stops))
    # print(stops)
    
    while stack:
        v = stack.pop()
        correct_path = [v]
        
        if v in stops:
            stops.remove(v)
            
            for w in stops_connected[v]:
                stack.append(w)
                correct_path.append(w)

    return correct_path

# USE AN AJASCENCY LIST
def main():
    # get input
    
    # n = int(input())
    
    # Key is each stop as string and value is a list of all connected stops
    # stops_connected = {}
    # for _ in range(n):
    #     line = input().split()
    #     stop1, stop2 = line[0], line[1]
        
    #     if stops_connected.get(stop1) == None:
    #         stops_connected[stop1] = []
    #         stops_connected[stop1].append(stop2)
    #     else:
    #         stops_connected[stop1].append(stop2)
        
    #     if stops_connected.get(stop2) == None:
    #         stops_connected[stop2] = []
    #         stops_connected[stop2].append(stop1)
    #     else:
    #         stops_connected[stop2].append(stop1)
    
    stops_connected = {'Hburg': ['JMU'], 'JMU': ['Hburg', 'Charlottesville'], 'Charlottesville': ['JMU']}
    
    # query = input().split()
    query = ['Hburg', 'Charlottesville']
    stack = []
    correct_path = search(stack, stops_connected, query[0], query[1])
    
    # print(stack)
    print(" ".join(correct_path))
    print()
    print(stops_connected)
    

if __name__ == "__main__":
    main()
