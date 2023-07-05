class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None


class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    def addEdge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node

    def printGraph(self):
        for i in range(self.V):
            print("\nVertex", i, end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next


if __name__ == "__main__":
    n = int(input("Enter Number of Vertices: "))
    m = int(input("Enter Number of Edges: "))
    graph = Graph(n)
    for i in range(m):
        u, v = map(int, input("Add Edge Between: ").split())
        graph.addEdge(u, v)
    graph.printGraph()
