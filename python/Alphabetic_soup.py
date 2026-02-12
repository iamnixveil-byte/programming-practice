str = input("Enter your word or sentence \n")

def AlphabicSoup(str):
    str = str.lower()
    str = list(str)
    
    str.sort()
    result = "".join(str) 
    
    return result
print(AlphabicSoup(str))