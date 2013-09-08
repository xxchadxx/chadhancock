import random

def GenList(size):
  lst = range(size)
  random.shuffle(lst)
  return lst

def Resevoir(resevoir_size, list_size):
  lst = GenList(list_size)
  resevoir = []
  for idx, value in enumerate(lst):
    if idx < resevoir_size:
      resevoir.append(value)
    else:
      r_value = random.randint(0, idx)
      if r_value < resevoir_size:
        resevoir[r_value] = value
  return resevoir
