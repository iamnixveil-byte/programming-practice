import os

target = input("Enter the target IP address or hostname: \n ")

output = os.system("ping -c 1"  +  target)

if output == 0 :
    print(f"{target} is UP")
    
else :
    print(f"{target} is DOWN")
    
