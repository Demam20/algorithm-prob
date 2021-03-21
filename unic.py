def unic(str1):
  dic ={}
  start = 0
  res = 0
  for i in range(len(str1)):
    if str1[i] in dic :
      start = max(start, dic[str1[i]]+1)
    dic[str1[i]] = i
    res = max(res, i-start+1)
  return res 

str1 = "abcabcbb"
print (unic(str1))    