


#randomisation

import random




'''
#you can get different code such as from your own code with import
import Heads_or_Tails



#generates a random number from 1 - 100
random_interger = random.randint(1, 100)

print(f"random number from 1 - 100 is : {random_interger}")


#how to generate a random float

random_float = random.random()


random_float *= 5

print(f"random float {random_float}")


'''


#https://docs.python.org/3/tutorial/datastructures.html#data-structures


'''

#lists
#allows you to store various data in one variable

states_of_america = ["Delaware", "Pennsylvania", "Texas", "Ohio", "New Jersey", "New York"]




#only prints out the first variable in the list starting from 0 - 4

print(states_of_america[0])
print(states_of_america[1])


#by putting -1 u start from the end and move backwards
print(states_of_america[-1])
print(states_of_america[-2])



#lets you modify a variable within the list to something else
states_of_america[3] = "Not Ohio"

print(states_of_america[3])




#adds a new variable to the end of the list
states_of_america.append("Dakota")
print(states_of_america[-1])



'''



fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes" ]


#nested lists
#nested lists are lists that contain lists

dirty_dozen = [fruits, vegetables]


print(dirty_dozen[0][1])















