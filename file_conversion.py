#https://www.stat.auckland.ac.nz/~paul/Reports/gridGraphviz/examples/example4.html
#https://graphviz.org/
#https://www.w3schools.com/python/python_file_write.asp
#https://www.geeksforgeeks.org/python-remove-all-values-from-a-list-present-in-other-list/
class FileConversion:
    def __init__(self):
        self.data_list = []
        self.shortest_path = []
        self.non_shortest_path = []
    
    def convert_files(self, input_file, output_file, W=True):
        #open input file 
        input_file = open(f"./{input_file}", 'r')
        input_file = input_file.readlines()

        #open dot file
        output_file = open(f"./{output_file}", 'w')
        output_file.write("graph road{\n")

        self.data_list = []
        used_list = []
        
        #splits the input file into an array
        for i in input_file:
            i = i.split(",")
            i[2] = float(i[2])
            self.data_list.append(i)
        
        for i in self.data_list:
            if ([i[1], i[0], i[2]] in used_list):
                continue

            used_list.append(i)
            
            if (W):
                if [i[0],i[1]] in self.shortest_path:
                    self.convert_to_dot_weight(i[0], i[1], i[2], output_file, "red")
                else:
                    self.convert_to_dot_weight(i[0], i[1], i[2], output_file, "black")
            else:
                if [i[0],i[1]] in self.shortest_path:
                    self.convert_to_dot(i[0], i[1], output_file, "red")
                else:
                    self.convert_to_dot(i[0], i[1], output_file, "black")

            output_file.write("\n")

        #close the dot file
        output_file.write("}")
        output_file.close()

    def split_paths(self, A, B):
        #gets the shortest path
        self.shortest_path = self.ShortestPath(A,B)

        #splits the shortest path from the main list
        self.non_shortest_path = [i for i in self.data_list if i not in self.shortest_path]
        
    def ShortestPath(self, A, B):
        #A and B are both variables that store a node
        #example path
        path = [["NWoodAvenue","NPineStreet"],["NPineStreet","starbucks"]] 
        return path

    def convert_to_dot_weight(self, A, B, weight, output, color):
         #write an edge (and node) to the dot file 
         output.write(f"\"{A}\" [shape = circle]\n")
         output.write(f"\"{B}\" [shape = circle]\n")
         output.write("\n")
         output.write(f"\"{A}\" -- \"{B}\" [label = {weight},color = \"{color}\"]\n")

    def convert_to_dot(self, A, B, output, color):
         #write an edge (and node) to the dot file 
         output.write(f"\"{A}\" [shape = circle]\n")
         output.write(f"\"{B}\" [shape = circle]\n")
         output.write("\n")
         output.write(f"\"{A}\" -- \"{B}\" [color = \"{color}\"]\n")

    def check_nodes(self, node):
        for i in self.data_list:
            if node in i:
                return True
        return False
            
