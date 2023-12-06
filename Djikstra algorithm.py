import heapq
def shortestPath(n, edges, src):
        #create adjacent list
        adjacent = {}
        for i in range(n):
            adjacent[i] = []
        
        #assign each node with adjacent cell
        for s, e, w in edges:
            adjacent[s].append([e, w])

        shortest_path = {}
        # create min heap
        shortest = [[0, src]]
        while shortest:
            w1, e1 = heapq.heappop(shortest)
            if e1 in shortest_path:
                continue
            shortest_path[e1] = w1
            for e2, w2 in adjacent[e1]:
                if e2 not in shortest_path:
                    heapq.heappush(shortest, [w1+w2, e2])
        
        return shortest_path
    
myDict = shortestPath(5, [[0,1,10], [0,2,3], [1,3,2], [2,1,4], [2,3,8], [2,4,2], [3,4,5]], 0)
myKeys = list(myDict.keys())
myKeys.sort()
sorted_dict = {i: myDict[i] for i in myKeys}

print(sorted_dict)


