
#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇


print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))

tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))

people = int(input("How many people to split the bill? "))



if tip_percentage == 10:
    tip = 1.10
elif tip_percentage == 12:
    tip = 1.12
elif tip_percentage == 15:
    tip = 1.15


pay = (bill/people)*tip

print(f"Each person should pay: ${round(pay, 2)}")









