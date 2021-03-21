def Ledder(arr,n ):
  max_led = arr[n-1]
  print (max_led,"")
  for i in range(n-2,-1,-1):
    
    if max_led < arr[i] :
      max_led = arr[i]
      print (max_led,"")
      

arr = [16,17,4,3,5,2] 
n = len(arr)  
Ledder(arr,n )   

