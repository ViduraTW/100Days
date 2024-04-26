
'''

#Uses a double digit number and adds the two digits together
num = int(input("Number?"))


str = str(num)

print(type(str))

str1 = int(str[0])
str2 = int(str[1])

mult = str1 + str2


print(mult)



#Band name generator
#1. Create a greeting for your program.

print("Welcome to a Band name generator")

#2. Ask the user for the city that they grew up in.

city = input("What city did you grow up in?\n")

#3. Ask the user for the name of a pet.

pet_name = input("Whats your pets name?\n")

#4. Combine the name of their city and pet and show them their band name.

print("A possible band name could be " + city + " " + pet_name)

#5. Make sure the input cursor shows on a new line:
# Solution: https://replit.com/@appbrewery/band-name-generator-end



#BMI calculator

height = input("Whats your height?")
weight = input("Whats your weight?")

#this turns the string input variables and turns them into floats
height = float(height)
weight = float(weight)

sq_h = height * height

BMI = weight / sq_h

#this turns the float variable with various decimal places into a whole number
print(int(BMI))



#Leap Year Calculator


year = int(input("Whats the year?"))


if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")

#This happens if the year has remainders when its divided by 4
else:
    print("Not Leap Year")




#Life in Weeks

age = input()

age_in_weeks = 52 * int(age)
weeks_left = str((90 * 52) - age_in_weeks)


print("You have " + weeks_left + " weeks left." )



#Odd or Even


number = int(input())

if number%2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")



#BMI 2.0

height = float(input())
weight = int(input())


BMI = weight / height ** 2


if BMI >= 35:
    print("Your BMI is " + str(BMI) + ", you are clinically obese")
elif 35 > BMI >= 30:
    print("Your BMI is " + str(BMI) + ", you are obese.")
elif 30 > BMI >= 25:
    print("Your BMI is " + str(BMI) + ", you are slightly overweight.")
elif 25 > BMI >= 18.5:
    print("Your BMI is " + str(BMI) + ", you have a normal weight.")
elif BMI < 18.5:
    print("Your BMI is " + str(BMI) + ", you are underweight.")


'''



#Pizza Order Practice

print("Thank you for choosing Python Pizza Deliveries!")
size = input("Size?") # What size pizza do you want? S, M, or L
add_pepperoni = input("Pepperoni?") # Do you want pepperoni? Y or N
extra_cheese = input("Cheese?") # Do you want extra cheese? Y or N
bill = 0



if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25


if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    elif size == "M" or "L":
        bill += 3
else:
    bill = bill


if extra_cheese == "Y":
    bill += 1


print(f"Your final bill is: ${bill}.")



































