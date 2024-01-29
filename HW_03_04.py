from datetime import datetime

def get_upcoming_birthdays(users):
    today = datetime.today().date() # Today date
    birthdays = [] # empty list for results
    for user in users:
        bday = datetime.strptime(user["birthday"], "%Y.%m.%d").date() #  getting birthday dates by key "birthday"
        bday_this_year = datetime(today.year, bday.month, bday.day).date() # change birthday year to current year
        if 0<=(bday_this_year - today).days<7:
            if datetime.weekday(bday_this_year) < 6:
               birthdays.append({'name':user['name'], 'birthday':(datetime.strftime(bday_this_year,"%Y.%m.%d"))}) # Add to list
            else: 
                if datetime.weekday(bday_this_year) == 5: # Saturday bday
                    bday_this_year = datetime(bday_this_year.year, bday_this_year.month, bday_this_year.day + 2).date() # Move to Monday
                    birthdays.append({'name':user['name'], 'birthday':(datetime.strftime(bday_this_year,"%Y.%m.%d"))}) # Add to list
                elif datetime.weekday(bday_this_year) == 6: # Sunday bday
                    bday_this_year = datetime(bday_this_year.year, bday_this_year.month, bday_this_year.day + 1).date() # Move to Monday
                    birthdays.append({'name':user['name'], 'birthday':(datetime.strftime(bday_this_year,"%Y.%m.%d"))}) # Add to list
    return birthdays

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
print(get_upcoming_birthdays(users))
