number = int(input("Enter your number \n"))

def Factorial(num):
    for i in range(num - 1):
        i *= num
        num += i
    return  num

print(Factorial(number))

