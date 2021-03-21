from collections import defaultdict

def freq(arr, n):
  d = defaultdict(lambda: 0)
  for i in range(n):
    d[arr[i]] += 1
  arr.sort(key=lambda x: (-d[x],x))
  return (arr)

arr= [2,5,2,8,5,6,8,8] 
n = len(arr) 
solution = freq(arr, n)
print (solution)