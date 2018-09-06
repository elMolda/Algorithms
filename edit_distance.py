def distance_bf(str1,str2):
  if len(str1) == 0:
    return len(str2)
  if len(str2) == 0:
    return len(str1)

  repl = distance_bf(str1[1:],str2[1:]) + cost(str1,str2,0,0)
  dele = distance_bf(str1[1:],str2) + 1
  inst = distance_bf(str1,str2[1:]) + 1

  return min(repl,dele,inst)
  
def cost(str1,str2,ind1,ind2):
  if str1[ind1] == str2[ind2]:
    return 0
  else:
    return 1

def distance_dyn(str1, str2):
  d = [0] * (len(str1)+1)
  for i in range(len(str1)+1):
    d[i] = [0] * (len(str2)+1)

  for i in range(1,len(str1)+1):
    for j in range(1,len(str2)+1):
      if str1[i-1] == str2[j-1]:
        d[i][j] = d[i-1][j-1]
      else:
        d[i][j] = 1 + min(d[i-1][j-1],d[i-1][j],d[i][j-1])

  return d[len(str1)][len(str2)]

print(distance_bf("tigre","trigo"))
print(distance_dyn("tigre","trigo"))

