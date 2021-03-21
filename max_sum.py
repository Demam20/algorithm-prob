def maxSubArraySum(a,size):
     
    max_so_far =0
    curr_max = 0
     
    for i in range(size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far,curr_max)
         
    return max_so_far
 
# Driver function to check the above function 
a = [-2,1,-3,4,-1,2,1,-5,4]
print("Maximum contiguous sum is" , maxSubArraySum(a,len(a)))