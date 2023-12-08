from collections import defaultdict,deque
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.path_possible = []
    
    def add_nodes(self,node_name):
        if node_name not in self.graph:
            self.graph[node_name] = []
            return
        print("node already exist")
    
    def add_edges(self,source,destination):
        if source not in self.graph or destination not in self.graph:
            print("source or destination is not present")
            return
        self.graph[source].append(destination)
    
    def print_graph(self):
        for n,e in self.graph.items():
            print("{} --> {}".format(n,e))
        
    def get_all_path(self,source,destination):
        visiting_list = {}
        path = []
        for i in self.graph:
            visiting_list[i] = False
        self.get_path(source,destination,visiting_list,path)

    def get_path(self,source,destination,visiting_list,path):
        visiting_list[source] = True
        path.append(source)
        if source == destination:
            print(path)
            self.path_possible.append(path.copy())
        else:
            for i in self.graph[source]:
                if visiting_list[i] == False:
                    self.get_path(i,destination,visiting_list,path)
        visiting_list[source] = False
        path.pop()
    
    def path_possible_print_smallest(self):
        minimum_path = self.path_possible[0]
        for i in self.path_possible[1:]:
            if len(minimum_path) > len(i):
                minimum_path = i
        print(minimum_path)
    
    def Bfs(self,starting_node):
        visited_nodes = set()
        que = deque([starting_node])
        result = []
        while que:
            cuurent_node = que.popleft()
            if cuurent_node not in visited_nodes:
                visited_nodes.add(cuurent_node)
                result.append(cuurent_node)
                neigh = []
                for i in self.graph[cuurent_node]:
                    if i not in visited_nodes:
                        neigh.append(i)
                que.extend(neigh)
        print(result)
        
g = Graph()
list_of_places = ['mumbai','goa','gujarat','rajasthan','delhi']
for i in list_of_places:
    g.add_nodes(i)
edges_list = {
    1 : ('mumbai','goa'),
    2 : ('mumbai', 'gujarat'),
    3 : ('gujarat','rajasthan'),
    4 : ('delhi','gujarat'),
    5 : ('goa','delhi'),
    6 : ('rajasthan','delhi'),
    7 : ('delhi','mumbai')
}
for i in edges_list.keys():
    u,v = edges_list[i]
    g.add_edges(u,v)
print('*'*20)
g.print_graph()
print('*'*20)
g.get_all_path('mumbai','delhi')
print('*'*20)
g.path_possible_print_smallest()
print('*'*20)
g.Bfs('goa')