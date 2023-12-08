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
            print("source or destination does not exist in the graph")
        self.graph[source].append(destination)
    
    def graph_display(self):
        for nodde,neighbours in self.graph.items():
            print("{} --> {}".format(nodde,neighbours))
    
    def Bfs(self,start_value):
        visited_list = set()
        que = deque([start_value])
        result = []
        while que:
            current_node = que.popleft()
            if current_node not in visited_list:
                visited_list.add(current_node)
                result.append(current_node)
                neighbours = []
                for i in self.graph[current_node]:
                    if i not in visited_list:
                        neighbours.append(i)
                que.extend(neighbours)
        print(result)
    
    def Dfs(self,start_value):
        visited_list = set()
        stack = deque([start_value])
        result = []
        while stack:
            cuurent_value = stack.pop()
            if cuurent_value not in visited_list:
                visited_list.add(cuurent_value)
                result.append(cuurent_value)
                neighbours = []
                for i in self.graph[cuurent_value]:
                    if i not in visited_list:
                        neighbours.append(i)
                stack.extend(neighbours)
        print(result)
    
    def get_path(self,source,destination,visiting_list,path):
        visiting_list[source] = True
        path.append(source)
        if source == destination:
            path_string = ''
            for i in path:
                path_string = "{} --> {} ".format(path_string,i)
            print(path_string)
        else:
            for i in self.graph[source]:
                if visiting_list[i] == False:
                    self.get_path(i,destination,visiting_list,path)
        visiting_list[source] = False
        path.pop()

    def get_all_path(self,source,destination):
        all_nodes = set()
        for node,neigh in self.graph.items():
            all_nodes.add(node)
        visiting_list = {}
        for i in all_nodes:
            visiting_list[i] = False
        path = []
        self.get_path(source,destination,visiting_list,path)
    

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
g.get_all_path(source, destination)
print()
g.Bfs('Home')
g.Dfs('Home')


