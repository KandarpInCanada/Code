from collections import defaultdict,deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.path_possible = []
    
    def add_nodes(self,number_value):
        if number_value not in self.graph:
            self.graph[number_value] = []
            return
        print("nodes already exist")
    
    def add_edges(self,source,destination):
        if source not in self.graph and destination not in self.graph:
            print("source or destination does not exist")
            return
        self.graph[source].append(destination)
    
    def print_graph(self):
        for n,e in self.graph.items():
            print("{} -> : {}".format(n,e))
    
    def get_all_path(self,source,destination):
        visiting_list = {}
        path = []
        all_nodes = set()
        for n,e in self.graph.items():
            all_nodes.add(n)
        for i in all_nodes:
            visiting_list[i] = False
        self.get_path(source,destination,visiting_list,path)
    
    def get_path(self,source,destination,visiting_list,path):
        visiting_list[source] = True
        path.append(source)
        if source == destination:
            print("Path : {}".format(path))
            self.path_possible.append(path.copy())
        else:
            for i in self.graph[source]:
                if visiting_list[i] == False:
                    self.get_path(i,destination,visiting_list,path)
        visiting_list[source] = False
        path.pop()
    
    def print_all_path(self):
        print(self.path_possible)

g = Graph()
nodes_list = [
    'Home',
    'Market',
    'Park',
    'McDonalds',
    'JuniorSchool',
    'University',
    'Lake',
    'BusTerminal'
]
for i in nodes_list:
    g.add_nodes(i)

edges_list = {
    1: ("Home", "Market"),
    2: ("Park", "Home"),
    3: ("Park", "McDonalds"),
    4: ("Park", "JuniorSchool"),
    5: ("McDonalds", "University"),
    6: ("Market", "JuniorSchool"),
    7: ("Market", "Lake"),
    8: ("JuniorSchool", "Market"),
    9: ("JuniorSchool", "BusTerminal"),
    10: ("Lake", "BusTerminal"),
    11: ("BusTerminal", "University")}
for i in edges_list.keys():
    u, v = edges_list[i]
    g.add_edges(u,v)

source, destination = "Home", "University"

print(f"Following are all different paths from  {source} to  {destination} :")
g.get_all_path(source, destination)
g.print_all_path()
