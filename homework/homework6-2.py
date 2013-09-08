def ListFromFile(filename):
  with open(filename, 'r') as f:
    return [int(line) for line in f]

class Heap(object):
  def __init__(self, lst=(), min_heap=True):
    self.heap = []
    if min_heap:
      self.cmp = lambda x, y: x < y
    else:
      self.cmp = lambda x, y: x > y
    for item in lst:
      self.Insert(item)
  def __str__(self):
    return str(self.heap)
  def __len__(self):
    return len(self.heap)
  def Swap(self, a, b):
    self.heap[a], self.heap[b] = self.heap[b], self.heap[a]
  def Insert(self, item):
    self.heap.append(item)
    idx = len(self) - 1
    while idx and self.cmp(item, self.Parent(idx)):
      idx = self.BubbleUp(idx)
  def Extract(self):
    if len(self) == 0:
      return None
    if len(self) == 1:
      return self.heap.pop()
    self.Swap(0, -1)
    min_val = self.heap.pop()
    idx = 0
    while idx is not None and not self.cmp(self.heap[idx], self.Child(idx)):
      idx = self.BubbleDown(idx)
    return min_val
  def ParentIndex(self, idx):
    return None if idx == 0 else (idx - 1) / 2
  def Parent(self, idx):
    parent = self.ParentIndex(idx)
    return None if parent is None else self.heap[parent]
  def BubbleUp(self, idx):
    parent = self.ParentIndex(idx)
    if parent is not None:
      self.Swap(parent, idx)
    return parent
  def ChildIndex(self, idx):
    idx2 = idx * 2 + 1
    children = []
    for x in (0, 1):
      try:
        children.append(self.heap[idx2 + x])
      except IndexError:
        pass
    if not children:
      return None
    if len(children) == 1:
      return idx2
    return idx2 if self.cmp(children[0], children[1]) else idx2 + 1
  def Child(self, idx):
    child = self.ChildIndex(idx)
    return None if child is None else self.heap[child]
  def BubbleDown(self, idx):
    child = self.ChildIndex(idx)
    if child is not None:
      self.Swap(child, idx)
    return child

class MedianHeap(object):
  def __init__(self, lst=()):
    self.median = None
    self.left = Heap(min_heap=False)
    self.right = Heap()
    for item in lst:
      self.Insert(item)
  def __str__(self):
    return 'left: %s\nmedian: %s\nright: %s' % (
        self.left, self.median, self.right)
  def Equality(self):
    return len(self.left) == len(self.right)
  def Insert(self, item):
    if self.median is None:
      self.median = item
    elif self.Equality():
      if item < self.median:
        self.left.Insert(item)
        self.right.Insert(self.median)
        self.median = self.left.Extract()
      else:
        self.right.Insert(item)
    else:
      if item < self.median:
        self.left.Insert(item)
      else:
        self.left.Insert(self.median)
        self.right.Insert(item)
        self.median = self.right.Extract()

def MedianMaint(lst):
  heap = MedianHeap()
  medians = []
  for item in lst:
    heap.Insert(item)
    medians.append(heap.median)
  print 'sum: %s' % sum(medians)
  return sum(medians) % 10000
