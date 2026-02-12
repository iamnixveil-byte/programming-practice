arr = list(map(int , input("Enter an array \n").split()))
arr.sort()
j = [ ]
for i in arr:
   if i > max(arr):
     j.append(i)
     
j = max(i)
print(j) 
