def rotLeft(a , d):
    d = d % len(a)
    return   a[  d: ] + a[  : d]
    

num = int(input())
arr = input().split(",") 
result = rotLeft(a = arr, d = num)
for x in result :
  print(x , end = " ")  
