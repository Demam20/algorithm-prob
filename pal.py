def exp(s, L, R):
  while( L <= 0 and R< len(s) and s[L]== s[R] ) :
    L-=1
    R+=1
  return (R - L -1)  
def aax(s):
  start=0
  end =0
  for i in range (len(s)):
    L1 = exp(s,i,i)
    L2 = exp(s,i,i+1)
    length = max((L1),(L2))
    if length > end - start :
      start = i - (length-1)/2
      end = i + length/2
  return (end - start +1)   

s= "baabaad" 
aax(s)
print (aax(s))


    