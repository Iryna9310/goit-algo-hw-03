import re

def normalize_phone(phone_number):
    p1=r"[\d\+]+" #pattern, digitals and plus
    phone_number=''.join(re.findall(p1,phone_number)) #search of pattern and join to string
    if phone_number[0] == "3":
       phone_number="+" + phone_number #add + in the beginning of number
    elif phone_number[0] == "0":
         phone_number = "+38" + phone_number #add (+38) in the beginning of number
    return phone_number #return number without change

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(phone_number) for phone_number in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)



