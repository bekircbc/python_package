def maxFinder(*params):
  current_max=params[0]
  for item in params:
    if item >current_max:
      current_max=item
  return current_max
  

def minFinder(*params):
  current_min=params[0]
  for item in params:
    if item < current_min:
      current_min=item
  return current_min
  

