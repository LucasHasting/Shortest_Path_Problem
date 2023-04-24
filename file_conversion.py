#https://www.stat.auckland.ac.nz/~paul/Reports/gridGraphviz/examples/example4.html
#https://graphviz.org/
#https://www.w3schools.com/python/python_file_write.asp
#https://www.geeksforgeeks.org/python-remove-all-values-from-a-list-present-in-other-list/
class FileConversion:
    def __init__(self):
        #initilize public variables
        self.data_list = []
        self.shortest_path = []
    
    def convert_files(self, input_file, output_file, W=True):
        #open input file 
        input_file = open(f"./{input_file}", 'r')
        input_file = input_file.readlines()

        #open dot file
        output_file = open(f"./{output_file}", 'w')
        output_file.write("graph road{\n")

        #declare the used list
        used_list = []
        
        #splits the input file into an data_list
        for i in input_file:
            i = i.split(",")
            i[2] = float(i[2])
            self.data_list.append(i)

        #creates the dot file
        for i in self.data_list:
            #if data is duplicated continue
            if ([i[1], i[0], i[2]] in used_list):
                continue

            #add the current list to the used list
            used_list.append(i)

            #if weight is selected
            if (W):

                #highights the shortest path
                if [i[0],i[1]] in self.shortest_path:
                    self.convert_to_dot_weight(i[0], i[1], i[2], output_file, "red")

                #adds the rest of the path
                else:
                    self.convert_to_dot_weight(i[0], i[1], i[2], output_file, "black")

            #if weight is not selected
            else:

                #highights the shortest path
                if [i[0],i[1]] in self.shortest_path:
                    self.convert_to_dot(i[0], i[1], output_file, "red")

                #adds the rest of the path
                else:
                    self.convert_to_dot(i[0], i[1], output_file, "black")

            #updates the datalist to not have any duplicated values
            self.data_list = used_list 

            #adds a new line in the dot file
            output_file.write("\n")

        #close the dot file
        output_file.write("}")
        output_file.close()
        
    def ShortestPath(self, A, B):
        #A and B are both variables that store a node
        #example path
        A = [i for i in self.data_list if A in i]
        print(A)
        path = [["NWoodAvenue","NPineStreet"],["NPineStreet","starbucks"]] 
        self.shortest_path = path

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
        #check if a node exists
        for i in self.data_list:
            if node in i:
                return True
        return False
            
