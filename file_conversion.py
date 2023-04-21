#https://www.stat.auckland.ac.nz/~paul/Reports/gridGraphviz/examples/example4.html
#https://graphviz.org/
#https://www.w3schools.com/python/python_file_write.asp
#https://www.geeksforgeeks.org/python-remove-all-values-from-a-list-present-in-other-list/
class FileConversion:
    def convert_files(self, input_file, output_file):
        #open input file 
        input_file = open(f"./{input_file}", 'r')
        input_file = input_file.readlines()

        #open dot file
        output_file = open(f"./{output_file}", 'w')
        output_file.write("graph road{\n")

        data_list = []
        
        #splits the input file into an array
        for i in input_file:
            i = i.split(",")
            i[2] = float(i[2])
            data_list.append(i)

        #split the shortest path from other paths
        self.split_paths(data_list)

        #add the non shortest path edges
        for i in self.non_shortest_path:
            self.convert_to_dot(i[0], i[1], i[2], output_file, "black")
            output_file.write("\n")

        #add the shortest path edges
        for i in self.shortest_path:
            self.convert_to_dot(i[0], i[1], i[2], output_file, "red")
            output_file.write("\n")

        #close the dot file
        output_file.write("}")
        output_file.close()

    def split_paths(self, data):
        #gets the shortest path
        self.shortest_path = self.ShortestPath()

        #splits the shortest path from the main list
        self.non_shortest_path = [i for i in data if i not in self.shortest_path]
        
    def ShortestPath(self):
        #example path, leave weights
        path = [["g","h", 10.0],["h","i", 5.0]] 
        return path

    def convert_to_dot(self, A, B, weight, output, color):
         #write an edge (and node) to the dot file 
         output.write(f"\"{A}\" [shape = circle]\n")
         output.write(f"\"{B}\" [shape = circle]\n")
         output.write("\n")
         output.write(f"\"{A}\" -- \"{B}\" [label = {weight},color = \"{color}\"]\n")
