def pairFunc(ar):
    res = { }
    i = 0
    for i in range(len(ar)):
        if ar[i] in res:
            res[ar[i]] += 1
        else:
            res.update({ar[i] : 1})

    total = [ ]
    for key, value in res.items():  
        if value % 2 == 0:
            key_pairs = value // 2
            for j in range(key_pairs):
               total.append(key)
        else:
            key_pairs = (value - 1) // 2
            for j in range(key_pairs):
               total.append(key)

    new_total = [ ]
    for item in total:
        new = item, item
        new_total.append(new)
        
    return  len(new_total)

arr = input("Enter your list \n").split(",")
result = pairFunc(arr)
print(result)

