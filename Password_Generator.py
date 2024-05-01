

#Password Generator Project
import random
import List as list




print("Welcome to the PyPassword Generator!")
number_of_letters= int(input("How many letters would you like in your password?\n"))
number_of_symbols = int(input(f"How many symbols would you like?\n"))
amount_of_numbers = int(input(f"How many numbers would you like?\n"))


password_list = []
password = ''


'''
letters = random.choices(list.letters, k=number_of_letters)

symbols = random.choices(list.symbols, k=number_of_symbols)

numbers = random.choices(list.numbers, k=amount_of_numbers)


password = letters + symbols + numbers

'''


for char in range(1, number_of_letters + 1):
    random_char = random.choice(list.letters)
    password_list += random_char

for sym in range(1, number_of_symbols + 1):
    random_sym = random.choice(list.symbols)
    password_list += random_sym

for num in range(1, amount_of_numbers + 1):
    random_num = random.choice(list.numbers)
    password_list += random_num
    random.shuffle(password_list)



for c in password_list:
    password += c



print(f"Your password is: {password}")












