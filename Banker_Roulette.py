


names = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']

import random



#this gets the total number of variables within a list and subtracts it by 1
list_size = (len(names) - 1)


#this uses the list_size variable from before to generate a randomised interger
random_interger = random.randint(0, list_size)


print(f"{names[random_interger]} is going to buy the meal today!")








