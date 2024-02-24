
import math

days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

def add_time(start, duration, optional_day=''):
    # convert to 24 hour time
    conversion = 0
    if 'PM' in start:
        start = start.replace('PM', '')
        conversion = 12
    if 'AM' in start: 
        start = start.replace('AM', '')
    
    # convert time into minutes
    start = start.split(':')
    start_hour, start_minute = start
    start = ((int(start_hour) + conversion) * 60) + int(start_minute)

    # convert duration to minutes
    duration = duration.split(':')
    duration_hour, duration_minute = duration
    duration = (int(duration_hour) * 60) + int(duration_minute)

    end_minutes = 0
    end_hours = 0
    end_days = 0
    # calc end time in minutes
    end_minutes = start + duration

    # convert end time to hours if necessary
    if end_minutes >= 60:
        end_hours = math.floor(end_minutes / 60)
        end_minutes = end_minutes % 60

    # convert end time to days if necessary
    if end_hours >= 24: 
        end_days = math.floor(end_hours / 24)
        end_hours = end_hours % 24


    # convert back to 12 hour time and convert to string
    end_time = ''
    end_minutes = str(end_minutes)
    if len(end_minutes) == 1: 
        end_minutes = '0' + end_minutes
    if end_hours >= 12:
        if end_hours > 12:
            end_hours -= 12
        end_hours = str(end_hours)
        if len(end_hours) == 1: 
            end_hours = '0' + end_hours
        end_time = end_hours + ':' + end_minutes + ' PM'
    else: 
        if end_hours == 00:
            end_hours += 12
        end_hours = str(end_hours)
        if len(end_hours) == 1:
            end_hours = '0' + end_hours
        end_time = end_hours + ':' + end_minutes + ' AM'

    # check day
    if optional_day != '':
        # find optional_day index in days list
        n = 0
        for day in days:
            if optional_day.lower() == day:
                break
            else:
                n += 1
        # find end day 
        n = n + end_days
        if n > 6: 
            n -= 7
        end_time += f', {days[n].capitalize()}'

    # format day string
    if end_days != 0: 
        if end_days == 1:
            end_time += ' (next day)'
        else:
            end_time += f' ({end_days} days later)'

    return f'{end_time}'



print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)