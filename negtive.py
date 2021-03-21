def subArraySum(arr, n, sum):
     
    Map = {}
    curr_sum= 0
    for i in range(n) :
      curr_sum = curr_sum + arr[i]
      if curr_sum == sum:
        print ( 0 , i)
        return
      if (curr_sum - sum) in Map :
        print (Map[curr_sum - sum]+1, i) 
        return
      Map[curr_sum] = i   
    print ("sorry")
#if __name__ == "__main__": 
arr = [10,2,-2,-20,10]
n = len(arr)
sum = -10
 
subArraySum(arr, n, sum)
 