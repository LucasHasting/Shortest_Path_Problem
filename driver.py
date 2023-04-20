#https://www.geeksforgeeks.org/python-call-function-from-another-file/
#https://www.geeksforgeeks.org/python-pil-image-open-method/s
from PIL import Image
from graphviz import Source
import os
from file_conversion import *

def main():
    #name input and output files
    input_file = "data.txt" 
    output_file = "data.dot"

    #convert files
    Roads = FileConversion()
    Roads.convert_files(input_file, output_file)

    #set the path the dot file is in
    path = f"./{output_file}"

    #read the dot file
    s = Source.from_file(path)

    #view the dot file
    s.view()

    

main()
