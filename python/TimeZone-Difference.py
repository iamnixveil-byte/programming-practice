def getSecond1(timestr1):
    time = timestr1.replace(":" , " ")
    time_count = time.split(" ")

    hours = int(time_count[0])
    minutes = int(time_count[1])
    sec =int(time_count[2])
    total_sec = (hours * 3600 ) + ( minutes * 60) + sec  
    timezone = time_count[3]
    
    if timezone.startswith("+"):
        timezone = timezone.removeprefix("+")
        timezone = list(timezone)
        tz_hours = timezone[0:2] 
        tz_hours = "".join(tz_hours)
        tz_minutes = timezone[2:4] 
        tz_minutes = "".join(tz_minutes)
        timezone =int(tz_hours )* 3600 + int(tz_minutes )* 60
        timezone = int(timezone)
        total_second1 =  total_sec + timezone 
    else:
        timezone = timezone.removeprefix("-")
        timezone = list(timezone)
        tz_hours = timezone[0:2] 
        tz_hours = "".join(tz_hours)
        tz_minutes = timezone[2:4] 
        tz_minutes = "".join(tz_minutes)
        timezone =int(tz_hours )* 3600 + int(tz_minutes )* 60
        timezone = int(timezone)
        total_second1 =  total_sec - timezone 
    return total_second1 
    
    
def getSecond2(timestr2):   
    time = timestr2.replace(":" , " ")
    time_count = time.split(" ")

    hours = int(time_count[0])
    minutes = int(time_count[1])
    sec =int(time_count[2])
    total_sec = (hours * 3600 ) + ( minutes * 60) + sec   
    timezone = time_count[3]
    
    if timezone.startswith("+"):
        timezone = timezone.removeprefix("+")
        timezone = list(timezone)
        tz_hours = timezone[0:2] 
        tz_hours = "".join(tz_hours)
        tz_minutes = timezone[2:4] 
        tz_minutes = "".join(tz_minutes)
        timezone =int(tz_hours )* 3600 + int(tz_minutes )* 60
        timezone = int(timezone)
        total_second2 =  total_sec + timezone 
    else:
        timezone = timezone.removeprefix("-")
        timezone = list(timezone)
        tz_hours = timezone[0:2] 
        tz_hours = "".join(tz_hours)
        tz_minutes = timezone[2:4] 
        tz_minutes = "".join(tz_minutes)
        timezone =int(tz_hours )* 3600 + int(tz_minutes )* 60
        timezone = int(timezone)
        total_second2 =  total_sec - timezone 
    return  total_second2 
     
timestr1 = input("Enter your post time \n")
timestr2 = input("Enter your the  time you saw the post \n")

print(abs(getSecond1(timestr1) - getSecond2(timestr2)))