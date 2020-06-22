class Graph:
    def __init__(self,num_node):
        self.adj_list = []
        for i in range (num_node):
            self.adj_list.append([])

    def addEdge(self,source,destination):
        self.adj_list[source].append(destination)
        self.adj_list[destination].append(source)

    def print(self):
        for i in self.adj_list:
            print(i)
        
    

S = Graph(5)
S.addEdge(1,4)
S.addEdge(1,2)
S.addEdge(3,4)
S.addEdge(2,3)
S.print()
