
def add_time(*args):
    
    #Setting up dictionary used for end day of week
    week_day = {"monday" : 1,
                "tuesday" : 2,
                "wednesday" : 3,
                "thursday" : 4,
                "friday" : 5,
                "saturday" : 6,
                "sunday" : 7}
    
    #Extracting variables    
    if len(args) == 3:    
        start_day = args[2].lower()
        
    start_hours = int(args[0][0:2].strip(":"))

    if args[0][-2:] == "PM":
        start_pm = True
    else:
        start_pm = False
    
    #Splitting added time into hours and minutes
    added_split = args[1].split(":")
    #Assigning added hours and minutes
    added_hours = int(added_split[0])
    added_mins = int(added_split[1])
    #Calculating total added minutes
    total_added_mins = added_hours * 60 + added_mins
    
    #Calculating start time as total minutes
    
    total_start_mins = start_hours * 60 + int(args[0][-5:-3])
    
    #Adding on 12 hours if PM (excluding noon)
    if (start_hours != 12) and (start_pm == True):
        total_start_mins += 720
    
    #Adding on 12 hours if midnight
    if (start_hours == 12) and (start_pm == False):
        total_start_mins += 720
    
    #Used to minus 24 hours off if time is between 12AM - 1AM
    if total_start_mins > 1440:
        total_start_mins -= 1440
    
    #Calculating number of days passed
    #Minutes needed for next day
    next_day_mins = 1440 - total_start_mins

    
    #Total number of days passed
    #Code used to prevent division with 0 as numerator
    if total_added_mins != next_day_mins:    
        
        #Calculates added days excluding the first
        days_passed = int((total_added_mins - next_day_mins) / 1440)
        
        #Calculates if the starting day is passed
        if total_added_mins > next_day_mins:
            days_passed += 1
            print(total_added_mins, next_day_mins)
        
        
    #If added minutes is equal to number needed to reach 12AM, no new day is reached (seconds are rounded down)
    else:
        days_passed = 0
    
    
    #Calculating the final time in the 12-hour clock format
    #Total minutes 
    total_final_mins = total_start_mins + total_added_mins
    
    #Total hours
    total_final_hours = int(total_final_mins / 60)
    
    #Digital hour of final time
    hours_in_final = total_final_hours - (24 * days_passed)
    displayed_hours = hours_in_final

    
    #Calculates AM / PM
    if hours_in_final >= 12:
        final_pm = "PM"
        #Subtracts Converts from digital to clock
        if hours_in_final > 12:
            displayed_hours -=12
    else:
        final_pm = "AM"
    
    #Sets hours to 12 if midnight
    if hours_in_final == 0:
        hours_in_final = 12
        displayed_hours = hours_in_final
    
    #Output minutes of final time
    mins_in_final = total_final_mins % 60
    
    #Final time
    final_time = (str(displayed_hours), ":", str(mins_in_final).zfill(2), " ", final_pm)
    final_time = ''.join(final_time)

    #Calculating the end day of the week
    if len(args) == 3:
        final_week_day_num = (days_passed + week_day[start_day]) % 7
        final_week_day = list(week_day)[final_week_day_num-1].capitalize()
    
    
    #Formatting new_time output
    new_time = final_time
    
    #Adds weekday 
    if len(args) == 3:
        new_time += ", "
        new_time += final_week_day
    
    #Adds days passed
    if days_passed == 1:
        new_time += " (next day)"
        
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"
    
    print(new_time)
    return new_time
