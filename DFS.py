class Graph:
    def __init__(self,node):
        self.graph = []
        for i in range(node):
            self.graph.append([])

    def addEdge(self,source,destination):
        self.graph[source].append(destination)

    def DFS(self,s):
        print("DFS")
        visited = [False] * (len(self.graph))
        stack = []
        stack.append(s)
        visited[s] = True

        while len(stack) > 0:
            s = stack.pop(len(stack)-1)
            print(s, end = " ")

            for i in self.graph[s]:
                if visited[i] == False:
                    stack.append(i)
                    visited[i] = True

    def print(self):
        for i in self.graph:
            print(i)


S = Graph(7)
S.addEdge(0,1)
S.addEdge(0,2)
S.addEdge(1,2)
S.addEdge(2,0)
S.addEdge(2,3)
S.addEdge(1,5)
S.addEdge(0,3)
S.addEdge(2,5)
S.addEdge(1,4)
S.addEdge(4,1)
S.addEdge(4,5)
S.addEdge(5,2)
S.addEdge(5,3)
S.DFS(2)
S.print()
