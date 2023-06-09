#https://www.geeksforgeeks.org/python-call-function-from-another-file/
#https://www.geeksforgeeks.org/python-pil-image-open-method/s
#https://stackoverflow.com/questions/41942109/plotting-the-digraph-with-graphviz-in-python-from-dot-file
from graphviz import Source
from file_conversion import *

def main():
    input_file = "data.txt" 
    output_file = "data.dot"
    Roads = FileConversion()
    Roads.convert_files(input_file, output_file, False)

    while True:
            print("Options:")
            print("1. Road with miles")
            print("2. See road without miles")
            print("3. Enter path")
            print("4. Quit")
            choice = input("Enter your choice (1-4): ")

            print()

            if choice == "1":
                pass
                #show_file(Roads, input_file, output_file, True)

            elif choice == "2":
                pass
                #show_file(Roads, input_file, output_file, False)

            elif choice == "3":
                vertex_a, vertex_b = get_check_node(Roads)

                if (vertex_a == 0):
                    continue

                Roads.split_paths(vertex_a, vertex_b)

            elif choice == "4":
                break

            else:
                print("Invalid choice. Please try again.")

'''    
def show_file(Road, inputf, outputf, weight=True):
    #convert files for unweighted
    Road.convert_files(inputf, outputf, weight)

    #set the path the dot file is in
    path = f"./{outputf}"

    #read the dot file
    s = Source.from_file(path)

    #view the dot file
    s.view()
'''

def get_check_node(Road):
    vertex_a = input("What is the starting vertex: ")
    if (not Road.check_nodes(vertex_a)):
        print("invalid vertex")
        return 0, 0

    vertex_b = input("What is the ending vertex: ")
    if (not Road.check_nodes(vertex_b)):
        print("invalid vertex")
        return 0, 0
    
    return vertex_a, vertex_b
    
main()
