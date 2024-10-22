def time_string(hours, minutes, time_format ):
    if minutes < 10:
        minutes_format = '0' + str(minutes)
    else:
        minutes_format = minutes
    if time_format == '24':
        if hours < 10:
            result = f'{'0'+ str(hours)}:{minutes_format}'
        else:    
            result = f'{hours}:{minutes_format}'
    elif time_format == '12':
        if hours >= 13:
            result = f'{hours - 12}:{minutes_format}pm'
        elif hours == 0:
            result = f'{hours + 12}:{minutes_format}am'
        else:
             result = f'{hours}:{minutes_format}am'
    else: 
        result = "Something wen wrong"
    return result 

print(time_string(15, 38, '24'))
print(time_string(13, 10, '12'))
print(time_string(0, 7, '12'))
print(time_string(8, 3, '24'))
print(time_string(0, 5 ,'24'))