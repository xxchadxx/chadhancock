import bisect

MIN = -10000
MAX = 10000

def ListFromFile(filename):
  with open(filename, 'r') as f:
    return sorted(int(line) for line in f)

def TwoSum(lst):
  sums = set()
  for x, item in enumerate(lst):
    start = bisect.bisect_left(lst, MIN - item)
    end = bisect.bisect_right(lst, MAX - item)
    for y in range(start, end):
      if y == x:
        continue
      total = lst[x] + lst[y]
      sums.add(total)
  return len(sums)
