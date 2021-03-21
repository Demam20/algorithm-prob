def kth(arr, n, k):
  arr.sort()
  print (arr[k-1]) 
   
arr = [7,10,4,3,20,15]  
n = len(arr) 
k = 4
kth(arr, n, k)