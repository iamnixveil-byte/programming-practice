def Count_string(string , substring):
    
    name = string.lower()
    name2 = substring.lower()
    name = list(string)
    name2 = list(substring)

    list_check  = [ ] 

    for i in range(len(name)):
      name3 = name[ i : len(name2 ) + i]
      
      name3 = "".join(name3)
      list_check.append(name3)
   
    name2 = "".join(name2)
    count = list_check.count(name2)
   
    return count

string = input("Enter your string \n").strip()
substring = input("Enter your substring \n").strip()

count = Count_string(string , substring )

print(count)