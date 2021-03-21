def sort( arr, n):
  count0 = 0
  count1 = 0
  count2 = 0
  for i in range(n):
    if arr[i] == 0:
      count0 +=1
    elif arr[i] == 1:
      count1 +=1
    elif arr[i] == 2:
      count2 +=1   
  
  for i in range(0,count0):
    arr[i] = 0
  for i in range(count0,(count0+count1)):
    arr[i] = 1
  for i in range((count0+count1),count2):
    arr[i] = 2  
  print (arr, n)    

arr = [0,2,0,1,0,1,2,2] 
n = len(arr) 
sort( arr, n)
