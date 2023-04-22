#https://www.geeksforgeeks.org/python-call-function-from-another-file/
#https://www.geeksforgeeks.org/python-pil-image-open-method/s
#https://stackoverflow.com/questions/41942109/plotting-the-digraph-with-graphviz-in-python-from-dot-file
from PIL import Image
from graphviz import Source
from file_conversion import *

def main():
    #name input and output files
    input_file = "data.txt" 
    output_file = "data.dot"
    show_file(input_file, output_file, True)
    

    
def show_file(inputf, outputf, weight=True):
    #convert files for unweighted
    Roads = FileConversion()
    Roads.convert_files(inputf, outputf, weight)

    #set the path the dot file is in
    path = f"./{outputf}"

    #read the dot file
    s = Source.from_file(path)

    #view the dot file
    s.view()
    
main()
