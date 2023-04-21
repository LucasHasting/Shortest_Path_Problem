filename = "data.txt"
with open(filename, "r") as f:
    data = [line.strip().split(",") for line in f]

graph = {}
for line in data:
    start = line[0]
    end = line[1]
    distance = int(line[2])
    
    if start not in graph:
        graph[start] = {}
    graph[start][end] = distance
    
print(graph)

#the first key-value pair {'g': {'h': 20}} represents a directed edge from node g to node h with a distance of 20.