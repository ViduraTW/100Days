
#Data Type


#Strings
#Strings are letters used
#you can use [] to figure out any element from a string
#subscripts start from 0
#you can also put negative numbers to reverse the order of where ur getting the element from


print("Hello"[-1])


#Integers
#Integers are whole numbers without any decimals
#Integers can be used to perform calculations

print(134 + 3523)

#you can use 123_244 in stead of , when writing out big numbers
#this allows you to visualise big numbers better and the computer ignores it

print(type(124_238_394))


#Float
#floats are numbers with decimals

print(type(3.1434546))


#Boolean
#Booleans are either True or False

print(type(True))
print(type(False))



#this provides us with an interger based on the number of characters typed in for the input
num_cha = len(input("What is your name?\n"))
print(num_cha)

#this lets you check the data type of a variable
print(type(num_cha))


#this allows you to transform an integer into a string
str_num_cha = str(num_cha)
print(str_num_cha)


print("Your name has " + str_num_cha + " characters")


#Math operators


#Addition
#Adds numbers using + sign

num1 = 33 + 23
print(num1)

#Subtraction
#Subtracts numbers together using - sign

num2 = 5 - 3
print(num2)

#Multiplication
#Multiplies different numbers using * sign

num3 = 5 * 3
print(num3)

#Division
#Divides different numbers using / sign
#Any time a number is divided it will become a float

num4 = 10 / 2
print(type(num4))
print(num4)

#Raising numbers to power
#Raises a number to the power of another number using ** two of these

num5 = 2 ** 3
print(num5)

#Rounding decimals
#The second number after comma lets u round the float to that number of decimal places
print(round(3.55555555, 4))


#Whole numbers from division
#By have // it turns it provides u with an integer
print(100 // 2)



number = 5 * 5
print(number)

#changes the value in number by subtracting 6
#this can be done with different operators as well
number -= 6
print(number)



#f strings

score = 2342
height = 2.5
is_True = True

#when f is typed in front of the string
#it allows you to be able to transform different data types all into strings without having to define each of them as a string
print(f"your score is {score} your height is {height} and this is {is_True}")
















































