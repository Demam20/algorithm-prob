def adjust(str1):
  st =[]
  i = 0
  while i < len(str1):
    if len(st)==0 or str1[i] != st[-1]:
      st.append(str1[i])
      i +=1
    else:
      st.pop() 
      i +=1
  if len(st) ==0 :
    return "empty"  
  else:
    new_string = " " 
    for i in st:
      new_string += str(i)  
    return (new_string)
str1 = "azxxzy" 
print (adjust(str1)) 

