number = int(input("Enter your number \n"))

def timeConvert(num):
        hours = 0
        minutes = 0
        seconds = 0
        if  num // 60 > 0  :
            hours = num // 60
        if num % 60  >=  0 :
            minutes = num % 60
        elif num % 60 > 0 :
              minutes = num // 60
        
        str = f"{hours} : {minutes}"        
            
        return str

print(timeConvert(number))