from queue import PriorityQueue

pq = PriorityQueue() # initialize 

pq.put((10,"blue")) # push a few values on the pq
pq.put((3, "green"))
pq.put((5, "purple"))
pq.put((11, "orange"))

while not pq.empty(): # pop in order (min queue)
    print(pq.get())