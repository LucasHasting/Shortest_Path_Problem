'''
Names: Lucas Hasting, Ethan Nix, Krutivas Pradhan
Assignment: 11
Date: 4/25/2023
File Description: converts a txt file met for grahs into a dot file to be viewed
Sources------------------------------------------------------------------------------------
https://www.stat.auckland.ac.nz/~paul/Reports/gridGraphviz/examples/example4.html
https://graphviz.org/
https://www.w3schools.com/python/python_file_write.asp
https://www.geeksforgeeks.org/python-remove-all-values-from-a-list-present-in-other-list/
https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/
https://docs.python.org/3/library/heapq.html
'''
import heapq

class FileConversion:

    #Constructor
    def __init__(self, file):
        #initilize public variables
        self.data_list = []
        self.shortest_path = []
        self.modify_data(file)

    '''
    Name: modify_data
    Description: gets the data from a file and into a 2D array
    Contribution: Lucas
    '''
    def modify_data(self, file):
        #open input file 
        file = open(f"./{file}", 'r')
        file = file.readlines()

        #delcare a temporary list that stores used edges
        used_list = []

        #splits the input file into an data_list
        for i in file:
            i = i.split(",")
            i[2] = float(i[2])
            self.data_list.append(i)

        #gets the data
        for i in self.data_list:

            #if data is duplicated continue
            if ([i[1], i[0], i[2]] in used_list):
                continue

            #add the current list to the used list
            used_list.append(i)

            #update the list
            self.data_list = used_list

    '''
    Name: convert_files
    Description: converts the data into a dot file
    Contribution: Lucas
    '''
    def convert_files(self, output_file, W=True):
        #open dot file
        output_file = open(f"./{output_file}", 'w')
        output_file.write("graph road{\n")        
        
        #creates the dot file
        for i in self.data_list:
            
            #if weight is selected
            if (W):
                #highights the shortest path
                if [i[0],i[1]] in self.shortest_path or [i[1], i[0]] in self.shortest_path:
                    self.convert_to_dot_weight(i[0], i[1], i[2], output_file, "red")
                #adds the rest of the path
                else:
                    self.convert_to_dot_weight(i[0], i[1], i[2], output_file, "black")

            #if weight is not selected
            else:

                #highights the shortest path
                if [i[0],i[1]] in self.shortest_path or [i[1], i[0]] in self.shortest_path:
                    self.convert_to_dot(i[0], i[1], output_file, "red")
                #adds the rest of the path
                else:
                    self.convert_to_dot(i[0], i[1], output_file, "black")

            #adds a new line in the dot file
            output_file.write("\n")

        #close the dot file
        output_file.write("}")
        output_file.close()


    '''
    Name: ShortestPath
    Description: Calculates the shortest path
    Contribution: Ethan
    '''
    def ShortestPath(self, A, B):
        # define a dictionary to store the graph
        graph = {}
        for i in self.data_list:
            if i[0] not in graph:
                graph[i[0]] = []
            graph[i[0]].append((i[1], i[2]))
            if i[1] not in graph:
                graph[i[1]] = []
            graph[i[1]].append((i[0], i[2]))
            
        # initialize variables
        distances = {}
        visited = set()
        previous = {}
        pq = []

        # set start node distance to 0 and add to priority queue
        distances[A] = 0
        heapq.heappush(pq, (0, A))

        # Dijkstra's Algorithm
        while pq:
            # get node with smallest distance from priority queue
            current_distance, current_node = heapq.heappop(pq)

            # if node has already been visited, continue to next node
            if current_node in visited:
                continue

            # mark node as visited
            visited.add(current_node)

            # update distances to neighbors and add to priority queue
            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight
                if neighbor not in distances or distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

        # construct shortest path from start to end
        path = []
        current_node = B
        while current_node != A:
            path.append(current_node)
            current_node = previous[current_node]
        path.append(A)
        path.reverse()

        #turn the path into a 2D array to work with convert_files function
        self.shortest_path = []
        for i in range(len(path)-1):
            self.shortest_path.append([path[i], path[i+1]])


    '''
    Name: convert_to_dot_weight
    Description: convert a node/edge to a dot file, includes the weight
    Contribution: Lucas
    '''
    def convert_to_dot_weight(self, A, B, weight, output, color):
         output.write(f"\"{A}\" [shape = circle]\n")
         output.write(f"\"{B}\" [shape = circle]\n")
         output.write("\n")
         output.write(f"\"{A}\" -- \"{B}\" [label = {weight},color = \"{color}\"]\n")


    '''
    Name: convert_to_dot
    Description: convert a node/edge to a dot file, does not include the weight
    Contribution: Lucas
    '''
    def convert_to_dot(self, A, B, output, color):
         output.write(f"\"{A}\" [shape = circle]\n")
         output.write(f"\"{B}\" [shape = circle]\n")
         output.write("\n")
         output.write(f"\"{A}\" -- \"{B}\" [color = \"{color}\"]\n")


    '''
    Name: check_nodes
    Description: check if a node exists
    Contribution: Lucas
    '''
    def check_nodes(self, node):
        for i in self.data_list:
            if node in i:
                return True
        return False
