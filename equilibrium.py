def equili (arr, n):
  left_sum = 0
  total_sum = sum(arr)
  Map = {}
  for i in range(n):
    left_sum = left_sum + arr[i]
    if (total_sum - left_sum) in Map and i<n-1:
      print (i)
    Map[left_sum] = i 

arr =[-7,1,5,2,-4,3,0] 
n = len(arr) 
equili (arr, n)
