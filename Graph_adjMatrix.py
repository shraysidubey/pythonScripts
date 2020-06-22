class Graph:
    def __init__(self,num_node):
        self.matrix = []
        for i in range (num_node):
             internal_list = []
            for j in range (num_node):
                internal_list.append(0)
            self.matrix.append(internal_list)
        print(self.matrix)

    def addEdge(self,source,destination):
        self.matrix[source][destination] = 1
        self.matrix[destination][source] = 1

    def print(self):
        for i in self.matrix:
            print(i)
        


S = Graph(5)
S.addEdge(0,4)
S.addEdge(1,2)
S.addEdge(3,4)
S.addEdge(2,3)
S.print()
