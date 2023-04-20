#https://stackoverflow.com/questions/49121491/issue-with-spacing-nodes-in-networkx-graph
#https://www.w3schools.com/python/python_classes.asp
#https://www.geeksforgeeks.org/python-remove-all-values-from-a-list-present-in-other-list/
#https://www.geeksforgeeks.org/python-remove-all-values-from-a-list-present-in-other-list/
#https://stackoverflow.com/questions/44267802/python-how-can-i-convert-a-2d-array-to-an-array-of-pairs
import matplotlib.pyplot as plt
from tkinter import *
import networkx as nx

class FileConversion:
    def __inist__(self):
        self.G = nx.Graph()
        self.text_size = 10

    def convert_files(self, input_file, output_file):
        input_file = open(f"./{input_file}", 'r')
        input_file = input_file.readlines()
        output_file = open(f"./{output_file}", 'w')
        ID = 1
        output_file.write("graph road{\n")
        for i in input_file:
            i = i.split(",")
            i[2] = float(i[2])

        self.split_paths(input_file)

        for i in self.non_shortest_path:
            try:
                i = i.split(",")
                i[2] = float(i[2])
            except:
                pass

            self.convert_to_dot(i[0], i[1], i[2], output_file, "black")
            output_file.write("\n")
            
        for i in self.shortest_path:
            try:
                i = i.split(",")
                i[2] = float(i[2])
            except:
                pass
            
            self.convert_to_dot(i[0], i[1], i[2], output_file, "red")
            output_file.write("\n")
        
        output_file.write("}")
        output_file.close()

    def split_paths(self, input_file):
        self.shortest_path = self.ShortestPath()

        #if not an array of pairs (2D array)
        self.shortest_path = [[x,y,z] for x,y,z in self.shortest_path]

        #splits the shortest path from the main list
        self.non_shortest_path = [i for i in input_file if i not in self.shortest_path]

        self.shortest_path =  [(x,y,z) for [x,y,z] in self.shortest_path]

    def ShortestPath(self):
        #example path, leave weights
        path = [["g","h", 10.0],["h","i", 5.0]] 
        return path

    def convert_to_dot(self, A, B, weight, output, color):
         output.write(f"\"{A}\" [shape = circle]\n")
         output.write(f"\"{B}\" [shape = circle]\n")
         output.write("\n")
         output.write(f"\"{A}\" -- \"{B}\" [weight = {weight} color = \"{color}\"]\n")
