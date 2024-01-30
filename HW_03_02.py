import random

def get_numbers_ticket(min, max, quantity):
    if min>=1 and max<1000 and quantity<=(max-min):
      list_of_numbers=list(range(min,max+1)) #range from which numbers will be chosen
      numbers=random.sample(list_of_numbers, quantity) #generate random numbers
      return (sorted(numbers)) #sorted random numbers
    else:
      empty_list=[]
      return (empty_list)

print(get_numbers_ticket(100,150,6))








