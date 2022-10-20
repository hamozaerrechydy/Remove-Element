def removeElement(list, delete): 
  n = [] 
  for x in list: 
    if x != delete: 
      n.append(x) 
  return n

print(removeElement([2,1,2,3, 2], 2)) 

"""
[x] create a new list 
[x] loop in the old list 
[x] if the current num does not equals to delete number push it to the new list  
"""
