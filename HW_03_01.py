from datetime import datetime

def get_days_from_today(date):
    current_date=datetime.today()  # today date
    try:
        convert_date=datetime.strptime(date, "%Y-%m-%d") # input date by user
    except ValueError:
        print("Input date has inccorect format") # error message
        exit()
    difference=current_date-convert_date  #difference of two dates
    print(difference.days) #output of difference

get_days_from_today("2023-01-20")



 
