#https://www.geeksforgeeks.org/python-call-function-from-another-file/
from network import *

def main():
    file = "data.txt" 
    Roads = VisualGraph()
    Roads.load_from_file(file)
    Roads.draw()

main()
