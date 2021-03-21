def first(s):
  for _ in range(len(s)):

    chars = s[0]
    if chars in s[1: ]:
      s = s.replace(chars, "")
      continue
    else:
      return chars
  return "_"    
s = "geekforgeek" 
print (first(s)) 
  