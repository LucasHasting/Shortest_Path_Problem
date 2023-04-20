#https://www.geeksforgeeks.org/python-call-function-from-another-file/
from PIL import Image
from graphviz import Source
import os
from file_conversion import *

def main():
    input_file = "data.txt" 
    output_file = "data.dot"
    
    Roads = FileConversion()
    Roads.convert_files(input_file, output_file)    
    path = f"./{output_file}"
    s = Source.from_file(path)
    s.view()

    

main()
