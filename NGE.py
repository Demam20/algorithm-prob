def next(arr,n):
  for i in range (n):
    next = -1
    for j in range (i+1,n):
      if arr[i]< arr[j]:
        next = arr[j]
        break
    print ( arr[i] ,next)

arr = [13,7,6,12]  
n = len(arr) 
next(arr,n)
 
        




