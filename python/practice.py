# def getSecond1(timestr1):
#     time = timestr1.replace(":" , " ")
#     time_count = time.split(" ")
    
#     hours = int(time_count[0])
#     minutes = int(time_count[1])
#     sec =int(time_count[2])
#     total_sec = (hours * 60 ) + ( minutes * 60) + sec  
#     timezone = time_count[3]
    
#     if timezone.startswith("+"):
#         timezone = timezone.removeprefix("+")
#         timezone = int(timezone)
#         timezone = timezone * 60
#         total_second1 =  total_sec + timezone 
#     else:
#         timezone = timezone.removeprefix("-")
#         timezone = int(timezone)
#         timezone = timezone * 60
#         total_second1 =  total_sec - timezone 
#     return timezone
# timestr1 = input("Enter something \n")
# print(getSecond1(timestr1))
  
Timezone = "2520"
Timezone = list(Timezone)

tz_hours = Timezone[0:2] 
tz_hours = "".join(tz_hours)
print(tz_hours)
tz_minutes = Timezone[2:4] 
tz_minutes = "".join(tz_minutes)

Timezone =int(tz_hours )* 3600 + int(tz_minutes )* 60
print(Timezone)