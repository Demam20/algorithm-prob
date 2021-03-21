def creat():
  stack =[]
  return stack
def isempty(stack):
  return len(stack)== 0

def push(stack,x):
  stack.append(x)

def pop (stack) :
  if isempty(stack):
    print ("error") 
  else:
    return stack.pop() 

def ngem(arr):
    s= creat()
    element= 0
    next = 0
    push(s, arr[0]) 
    for i in range (1,n):
      next= arr[i]  
      if isempty(s)== False:
        element= pop(s)
        while element < next :
          print ( str(element), "--", str(next))
          if isempty(s) == True:
            break
          element = pop(s)
        if element> next :
           push(s, element)

      push(s, next) 
    while  isempty(s) == False:
      element = pop(s)
      next = -1 
      print (str(element),"--- ", str(next))

arr =[4,5,2,25] 
n= len(arr) 
ngem(arr)




