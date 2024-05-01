



line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() #Wh ere do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇






#.lower makes the letter at that position into lowercase
letter = position[0].lower()
abc = ["a", "b", "c"]


#the index function provides us with the positioning of the letter within the list starting from 0 - 2
letter_index = abc.index(letter)


#This code obtains the variable at position 1 transforming it into an interger
#Then it subtracts it by 1 to assist in positionng for lists
number_index = int(position[1]) - 1


map[number_index][letter_index] = "X"








'''

letter = position[0].upper()
number = int(position[1]) - 1

if letter == "A":
    if number == 0:
        line1[0] = 'X'
    elif number == 1:
        line2[0] = 'X'
    elif number == 2:
        line3[0] = 'X'
elif letter == "B":
    if number == 0:
        line1[1] = 'X'
    elif number == 1:
        line2[1] = 'X'
    elif number == 2:
        line3[1] = 'X'
elif letter == "C":
    if number == 0:
        line1[2] = 'X'
    elif number == 1:
        line2[2] = 'X'
    elif number == 2:
        line3[2] = 'X'

'''






# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")