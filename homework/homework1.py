def ListFromFile(filename):
  with open(filename, 'r') as f:
    return [int(line) for line in f]

class Sorter(object):
  def Mergesort(self, lst):
    # Base case.
    if len(lst) < 2:
      return lst, 0
    # Recursively sort each half.
    half = len(lst) / 2
    left, left_inv = self.Mergesort(lst[:half])
    right, right_inv = self.Mergesort(lst[half:])
    # Merge results.
    result = []
    i = 0
    j = 0
    inv = left_inv + right_inv
    while i < len(left) and j < len(right):
      # Left side is smaller, add item and increment pointer.
      if left[i] < right[j]:
        result.append(left[i])
        i += 1
      # Right side is smaller, add item.
      else:
        result.append(right[j])
        j += 1
        inv += len(left) - i
    # Add whatever is left over.
    result.extend(left[i:])
    result.extend(right[j:])
    return result, inv
