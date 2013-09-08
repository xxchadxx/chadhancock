INFINITY = 1000000
TARGETS = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]

def AdjacencyListFromFile(filename):
  adjacency_list = {}
  with open(filename, 'r') as f:
    for line in f:
      values = line.split()
      node = int(values.pop(0))
      edges = []
      for edge in values:
        str_edge = edge.split(',')
        edges.append((int(str_edge[0]), int(str_edge[1])))
      adjacency_list[node] = (edges)
  return adjacency_list

def Dijkstra(g, source, target):
  nodes = g.keys()
  distances = {node: INFINITY for node in nodes}
  distances[source] = 0
  new_distances = {}
  while nodes:
    closest_node = sorted(distances, key=distances.get)[0]
    nodes.remove(closest_node)
    if distances[closest_node] == INFINITY:
      break
    for edge, weight in g[closest_node]:
      if edge in nodes:
        new_distance = distances[closest_node] + weight
        if new_distance < distances[edge]:
          distances[edge] = new_distance
    new_distances[closest_node] = distances.pop(closest_node)
  return new_distances[target]

def ShortestPaths(g):
  paths = [Dijkstra(g, 1, target) for target in TARGETS]
  print ','.join(str(p) for p in paths)
