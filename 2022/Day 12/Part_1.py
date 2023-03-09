from queue import PriorityQueue

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.edges = [[-1 for i in range(vertices)] for j in range(vertices)]
        self.visited = []
        self.e = 0

    def add_edge(self, u, v):
        self.edges[u][v] = 1
        self.e += 1

    def dijkstra(graph, start_vertex):
        D = {v:float('inf') for v in range(graph.v)}
        P = {v:None for v in range(graph.v)}
        D[start_vertex] = 0

        pq = PriorityQueue()
        pq.put((0, start_vertex))

        while not pq.empty():
            (dist, current_vertex) = pq.get()
            graph.visited.append(current_vertex)

            for neighbor in range(graph.v):
                if graph.edges[current_vertex][neighbor] != -1:
                    distance = graph.edges[current_vertex][neighbor]
                    if neighbor not in graph.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
                            P[neighbor] = current_vertex
        return D, P

sample = 1
f = open("sample.txt" if sample else "input.txt", 'r')
arr = []
i, j = 0, 0

for line in f:
    temp = []
    line = line.strip()
    j = 0
    for letter in line:
        if letter == "S":
            s = (i, j)
            temp.append(0)
        elif letter == "E":
            e = (i, j)
            temp.append(25)
        else:
            temp.append(ord(letter) - 97)
        j += 1
    arr.append(temp)
    i += 1

src = s[0] * len(arr[0]) + s[1]
dest = e[0] * len(arr[0]) + e[1]

g = Graph(len(arr)*len(arr[0]))

for i in range(len(arr)):
    for j in range(len(arr[0])):
        for adj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
            if adj[0] >= 0 and adj[0] < len(arr) and adj[1] >= 0 and adj[1] < len(arr[0]):
                if arr[i][j]+1 >= arr[adj[0]][adj[1]]:
                    g.add_edge(j+(i*len(arr[0])), adj[1]+(adj[0]*len(arr[0])))

D, P = Graph.dijkstra(g, src)
print(D[dest])

# current = dest 
# path = []
# while P[current] != None and current != src:
#     path.append(current)
#     current = P[current]
# path.append(dest)
# path.reverse()
# print(path)