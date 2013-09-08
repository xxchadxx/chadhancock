import random
import datetime
import itertools

def most_common(lst):
  groups = itertools.groupby(sorted(lst))
  def _auxfun((item, iterable)):
    return len(list(iterable)), -lst.index(item)
  return max(groups, key=_auxfun)[0]

def AdjacencyListFromFile(filename):
  adjacency_list = {}
  with open(filename, 'r') as f:
    for line in f:
      values = [int(x) for x in line.split()]
      adjacency_list[values[0]] = values[1:]
  return adjacency_list

def MinCut():
  graph = AdjacencyListFromFile('kargerMinCut.txt')
  while len(graph) > 2:
    # Get random nodes from graph.
    nodes = graph.keys()
    node1_index = random.choice(nodes)
    # node2_index = random.choice(graph[node1_index])
    node2_index = most_common(graph[node1_index])
    # Remove self-loops.
    while node2_index in graph[node1_index]:
      graph[node1_index].remove(node2_index)
    while node1_index in graph[node2_index]:
      graph[node2_index].remove(node1_index)
    # Collapse the two node edges.
    graph[node1_index].extend(graph.pop(node2_index))
    # Update all edges.
    for edges in graph.itervalues():
      while node2_index in edges:
        edges.remove(node2_index)
        edges.append(node1_index)
  # Min-cut should be the size of either of the edge's sets.
  node = random.choice(graph.keys())
  return len(graph[node])

def MinMinCut():
  cut_values = set()
  for x in range(105437):  # 200 choose 2 * ln(200)
    if x % 500 == 1:
      print 'Loop: %s at %s' % (x, datetime.datetime.now())
      print 'Current min cut: %s' % min(cut_values)
    cut_values.add(MinCut())
  print 'Min cut: %s', min(cut_values)
