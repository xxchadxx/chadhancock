import collections

def AdjacencyListFromFile(filename):
  adjacency_list = collections.defaultdict(list)
  with open(filename, 'r') as f:
    for line in f:
      values = [int(x) for x in line.split()]
      adjacency_list[values[0]].append(values[1])
  return adjacency_list

def ReverseGraph(graph):
  reversed_graph = collections.defaultdict(list)
  for node, edges in graph.iteritems():
    for edge in edges:
      reversed_graph[edge].append(node)
  return reversed_graph

def DFS(graph, node, discovered, ranking):
  stack = [node]
  while stack:
    new_node = stack[-1]
    discovered.add(new_node)
    for edge in graph[new_node]:
      if edge not in discovered:
        stack.append(edge)
        break
    else:
      stack.pop()
      ranking.append(new_node)
  return discovered, ranking

def SCC(graph):
  # Reverse all edges in graph for first DFS.
  reversed_graph = ReverseGraph(graph)
  nodes = reversed_graph.keys()
  num_nodes = len(nodes)
  discovered = set()
  ranking = []
  # Loop until all nodes are in the stack.
  print 'starting DFS 1'
  while nodes:
    # Choose an abritrary node to do DFS on, if it isn't in the stack yet.
    node = nodes.pop()
    if node not in discovered:
      discovered, ranking = DFS(reversed_graph, node, discovered, ranking)
  # DFS again to get the strongly connected components of original graph.
  scc_list = []
  discovered = set()
  print 'starting DFS 2'
  while ranking:
    node = ranking.pop()
    if node not in discovered:
      discovered, scc = DFS(graph, node, discovered, [])
      scc_list.append(len(scc))
  scc_list.sort(reverse=True)
  # Fill in some empty values to ensure we have at least 5.
  while len(scc_list) < 5:
    scc_list.append([])
  return scc_list[:10]
