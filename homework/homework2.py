def ListFromFile(filename):
  with open(filename, 'r') as f:
    return [int(line) for line in f]

def SwapItemsInList(lst, x, y):
  if x != y:
    lst[x], lst[y] = lst[y], lst[x]

def GetMiddle(x):
  return x / 2 if x % 2 != 0 else (x - 1) / 2

def ChoosePartition(lst):
  first = lst[0]
  last = lst[len(lst) - 1]
  mid = GetMiddle(len(lst))
  middle = lst[mid]
  median = sorted([first, middle, last])[1]
  return 0 if first == median else mid if middle == median else len(lst) - 1

class Sorter(object):
  def Quicksort(self, lst):
    # Base case.
    if len(lst) < 2:
      return lst, 0
    # Move the partition to the front.
    SwapItemsInList(lst, 0, ChoosePartition(lst))
    i = 1
    partition = lst[0]
    for j in range(1, len(lst)):
      # Item is smaller than partition, swap it and increment i pointer.
      if lst[j] < partition:
        SwapItemsInList(lst, i, j)
        i += 1
    # Done partitioning, put the partition in place.
    SwapItemsInList(lst, 0, i - 1)
    # Recursively sort and put it all together.
    left, left_comp = self.Quicksort(lst[:i - 1])
    right, right_comp = self.Quicksort(lst[i:])
    comparisons = left_comp + right_comp + len(lst) - 1
    return left + [partition] + right, comparisons
