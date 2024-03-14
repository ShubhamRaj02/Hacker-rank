# Problem name :-> Time Conversion
def timeConversion(s):
    # Extract hours, minutes, and seconds from the input string
    hours, minutes, seconds = map(int, s[:-2].split(':'))
    # Extract AM or PM from the input string
    period = s[-2:]
    
    # Convert to 24-hour format
    if period == 'PM' and hours != 12:
        hours += 12
    elif period == 'AM' and hours == 12:
        hours = 0
    
    # Format the time in 24-hour format
    return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)