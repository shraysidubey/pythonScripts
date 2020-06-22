class Graph:
    def __init__(self,node):
        self.graph = []
        for i in range(node):
            self.graph.append([])

    def addEdge(self,source,destination):
        self.graph[source].append(destination)

    def BFS(self,s):
        print("BFS")
        visited = [False] * (len(self.graph))
        queue = []
        queue.append(s)
        visited[s] = True

        while len(queue) > 0:
            s = queue.pop(0)
            print(s, end = " ")

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
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
S.BFS(2)
S.print()
