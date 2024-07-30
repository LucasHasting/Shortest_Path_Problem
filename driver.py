'''
Names: Lucas Hasting, Ethan Nix, Krutivas Pradhan
Assignment: 11
Date: 4/25/2023
File Description: driver function to show a menu and convert files
Sources----------------------------------------------------------------------------------------------------
https://www.geeksforgeeks.org/python-call-function-from-another-file/
https://www.geeksforgeeks.org/python-pil-image-open-method/s
https://stackoverflow.com/questions/41942109/plotting-the-digraph-with-graphviz-in-python-from-dot-file
'''
from graphviz import Source
from file_conversion import *
from extra_functions import *

def main():
    #name input and output files
    input_file = "Test_Plan.txt" 
    output_file = "data.dot"

    #create file conversion object
    Roads = FileConversion(input_file)

    #convert the file for a basic map
    Roads.convert_files(output_file, False)

    #menu to select options - done by Krutivas
    while True:
            print("Options:")
            print("1. Road with miles")
            print("2. See road without miles")
            print("3. Enter path")
            print("4. Quit")
            choice = input("Enter your choice (1-4): ")

            print()

            if choice == "1":
             show_file(Roads, input_file, output_file, True)

            elif choice == "2":
                show_file(Roads, input_file, output_file, False)

            elif choice == "3":
                vertex_a, vertex_b = get_check_node(Roads)

                if (vertex_a == 0):
                    continue

                Roads.ShortestPath(vertex_a, vertex_b)

            elif choice == "4":
                break

            else:
                print("Invalid choice. Please try again.")
    
main()
