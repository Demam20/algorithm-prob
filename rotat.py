def rotated( str1, str2):
  if len(str1) != len (str2):
    return "false"
  new = str1 + str1  
  if str2 in new :
    return "True"
  else:
    return "no"  
str1 = "amazon" 
str2 = "azonan"
print (rotated( str1, str2))