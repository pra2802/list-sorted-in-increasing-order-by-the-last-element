def last(n):return n[-1]
def sort(tuple): 
  return sorted(tuple,key=last)
print(sort([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
