from datetime import datetime

def get_days_from_today(date):
    current_date=datetime.today()  # today date
    try:
        convert_date=datetime.strptime(date, "%Y-%m-%d") # input date by user
    except ValueError:
        return ("Input date has inccorect format") # error message
    difference=current_date-convert_date  #difference of two dates
    return (difference.days) #output of difference

print(get_days_from_today("2024.01-20"))




 
