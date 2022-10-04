

def only_evens(new_list:list[int]) -> list():
  """Creates a new list of even values from the inputted list."""
  x_list: list[int] = list()
  i: int = 0 
  while i < len(x):
    if new_list[i] % 2 == 0:
      x_list.append(new_list[i])
    i = i +1
  return x_list
 
     
def concat( a:list[int], b: list[int]) -> list():
  """Creates a new list of combining the two list consectutively"""
  i: int = 0 
  x: list[int] = list () 
  while i < len(a):
    x.append(a[i])
    i +=1 
  while i < len(b):
    x.append(b[i])
    i += 1
  return x
   
  
def sub (a_list: list[int], start_index: int, end_index: int ) -> list():
  """Generates a list which is a subset of list, between a specified start and end index."""
  i: int = 0 
  x: list[int] = list()
  if len(a_list) == 0:
    return x 
  
  if start_index > len(a_list):
    return x 
  
  if end_index <= 0:
    return x
  
  while i < len(a_list):
    if a_list[i] == a_list[start_index]:
      x.append(a_list[start_index])
    
    if a_list[i] == a_list[end_index]:
      x.append(a_list[end_index - 1]) 
    else:
      if start_index < 0:
        start_index = 0
        x.append(a_list[start_index]) 
    i = i + 1
  if end_index > len(a_list):
    end_index = len(a_list) - 1
    x.append(a_list[end_index])
  return x 
  


def sub (a_list: list[int], start_index: int, end_index: int ) -> list():
  """Generates a list which is a subset of list, between a specified start and end index."""
  x_list: list[int] = list()
  if start_index < 0:
    start_index = 0
  if end_index > len(a_list):
    end_index = len(a_list) - 1 
  if len(a_list) == 0:
    return x_list 
  
  elif start_index < len(x_list):
    while start_index < end_index:
      x_list.append(a_list[start_index])
      start_index += 1 
  return x_list

def sub (a_list: list[int], start_index: int, end_index: int ) -> list():
  i: int = -1 
  x: list[int] = list()
  while i < len(a_list):
    if a_list[i] == a_list[start_index - 1]:
      x.append(a_list[start_index])

    if a_list[i] == a_list[end_index - 1]:
      x.append(a_list[end_index - 1])
    i = i + 1
  return x 

def sub (a_list: list[int], start_index: int, end_index: int ) -> list():
  i: int = 0 
  x: list[int] = list()
  if len(a_list) == 0:
    return x 
  
  if start_index > len(a_list):
    return x 
  
  if end_index <= 0:
    return x
  
  if start_index < 0:
    start_index = 0
    x.append(a_list[start_index])

  if end_index > len(a_list):
    end_index = len(a_list) - 1
    x.append(a_list[end_index])
    return x 
    

  while i < len(a_list):
    if a_list[i] == a_list[start_index]:
      x.append(a_list[start_index])
    
    if a_list[i] == a_list[end_index]:
      x.append(a_list[end_index - 1]) 
    i = i + 1
  return x 
  




def sub (a_list: list[int], start_index: int, end_index: int ) -> list():
  i: int = 0 
  x: list[int] = list()
  if len(a_list) == 0:
    return x 
  
  if start_index > len(a_list):
    return x 
  
  if end_index <= 0:
    return x
  
  while i < len(a_list):
    if a_list[i] == a_list[start_index]:
      x.append(a_list[start_index])
    
    if a_list[i] == a_list[end_index]:
      x.append(a_list[end_index - 1]) 
    else:
      if start_index < 0:
        start_index = 0
        x.append(a_list[start_index]) 
    i = i + 1
  if end_index > len(a_list):
    end_index = len(a_list) - 1
    x.append(a_list[end_index])
  return x 


