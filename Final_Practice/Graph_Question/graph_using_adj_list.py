from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_nodes(self,node_value):
        if node_value not in self.graph:
            self.graph[node_value] = []
            return
        print("node already exist")
    
    def add_edges(self,source,destination):
        if source not in self.graph or destination not in self.graph:
            print("source destination node does not exist")
            return
        self.graph[source].append(destination)
    
    def display_graph(self):
        for node,neighbours in self.graph.items():
            print("{} --> {}".format(node,neighbours))

    def Bfs_traversal(self,start_node):
        visited_node = set()
        que = deque([start_node])
        result = []
        while que:
            current_value = que.popleft()
            if current_value not in visited_node:
                result.append(current_value)
                visited_node.add(current_value)
                neigh_not_visited = []
                for i in self.graph[current_value]:
                    if i not in visited_node:
                        neigh_not_visited.append(i)
                que.extend(neigh_not_visited)
        print(result)
    
    def Dfs_traversal(self,start_node):
        visited_node = set()
        que = deque([start_node])
        result = []
        while que:
            current_value = que.pop()
            if current_value not in visited_node:
                result.append(current_value)
                visited_node.add(current_value)
                neigh_not_visited = []
                for i in self.graph[current_value]:
                    if i not in visited_node:
                        neigh_not_visited.append(i)
                que.extend(neigh_not_visited)
        print(result)

    def get_bus_route(self,source,destination):
        all_nodes = set()
        for node,neighbours in self.graph.items():
            all_nodes.add(node)
        visited_node_list = {}
        path = []
        for i in all_nodes:
            visited_node_list[i] = False
        self.get_visited_paths(source,destination,visited_node_list,path)
    
    def get_visited_paths(self,source,destination,visited_node_list,path):
        visited_node_list[source] = True
        path.append(source)
        if source == destination:
            path_string = ''
            for i in path:
                path_string = "{} -> {}".format(path_string,i)
            print(path_string)
        else:
            for i in self.graph[source]:
                if visited_node_list[i] == False:
                    self.get_visited_paths(i,destination,visited_node_list,path)
        visited_node_list[source] = False
        path.pop()

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
print()
g.get_bus_route(source, destination)
print()
g.Bfs_traversal('Home')
g.Dfs_traversal('Home')

