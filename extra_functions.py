'''
Name: show_file
Description: shows the file produced from the dot file
Contribution: Lucas
'''
def show_file(Road, inputf, outputf, weight=True):
    #convert files
    Road.convert_files(outputf, weight)

    #set the path the dot file is in
    path = f"./{outputf}"

    #read the dot file
    s = Source.from_file(path)

    #view the dot file
    s.view()

'''
Name: get_check_node
Description: gets a vertex and verifies that it exists
Contribution: Lucas
'''
def get_check_node(Road):

    #get the starting vertex and check if it exists
    vertex_a = input("What is the starting vertex: ")
    if (not Road.check_nodes(vertex_a)):
        print("invalid vertex")
        return 0, 0

    #get the ending vertex and check if it exists
    vertex_b = input("What is the ending vertex: ")
    if (not Road.check_nodes(vertex_b)):
        print("invalid vertex")
        return 0, 0

    #return the verticies
    return vertex_a, vertex_b
