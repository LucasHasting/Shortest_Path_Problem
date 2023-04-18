#https://stackoverflow.com/questions/49121491/issue-with-spacing-nodes-in-networkx-graph
#https://www.w3schools.com/python/python_classes.asp
#https://www.geeksforgeeks.org/python-remove-all-values-from-a-list-present-in-other-list/
#https://www.geeksforgeeks.org/python-remove-all-values-from-a-list-present-in-other-list/
#https://stackoverflow.com/questions/44267802/python-how-can-i-convert-a-2d-array-to-an-array-of-pairs
import matplotlib.pyplot as plt
import networkx as nx

class VisualGraph:
    def __init__(self):
        self.G = nx.Graph()

    def load_from_file(self, file):
        file = open(f"./{file}")
        file = file.readlines()
        for i in file:
            i = i.split(",")
            i[2] = float(i[2])
            self.G.add_edge(i[0], i[1], weight=i[2])
            #k is the distance ebtween the nodes
            self.pos = nx.spring_layout(self.G, k=len(self.G.edges), seed=7)  

    def draw(self):
        # nodes
        nx.draw_networkx_nodes(self.G, self.pos, node_size=700)

        shortest_path = self.ShortestPath()

        #if not an array of pairs (2D array)
        shortest_path = [(x,y) for x,y in shortest_path]

        #splits the shortest path from the main list
        non_shortest_path = [i for i in self.G.edges if i not in shortest_path]

        # shortest path edges
        nx.draw_networkx_edges(self.G, self.pos, edge_color='r',
                               edgelist = shortest_path, width=6)

        #other edges
        nx.draw_networkx_edges(self.G, self.pos,
                               edgelist = non_shortest_path, width=6)

        # node labels
        nx.draw_networkx_labels(self.G, self.pos, font_size=20, font_family="sans-serif")

        # edge weight labels
        edge_labels = nx.get_edge_attributes(self.G, "weight")
        nx.draw_networkx_edge_labels(self.G, self.pos, edge_labels)

        # plot
        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")
        plt.tight_layout()
        plt.show()

    def ShortestPath(self):
        #possible example, could also do an array of pairs
        array = [["g","h"],["h","i"]] 
        #array of pairs
        array2 = [("g","h"),("h","i")]
        return array



