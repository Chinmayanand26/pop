li = list()
for i in range (10):
  li.append(i)
  print("list:",li)
  
  i=0
  while i <len(li):
    li.pop(i)
    i+1
    print("final list",li)
  
