import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


RPS = [rock, paper, scissors]

computer_choice = random.randint(0, 2)


user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))



print(f"You chose {RPS[user]} ")


print(f"Computer chose {RPS[computer_choice]}")


if computer_choice == 0:
    if user == 0:
        print("Its a draw")
    elif user == 1:
        print("You Lose")
    elif user == 2:
        print("You Win")
elif computer_choice == 1:
    if user == 0:
        print("You Lose")
    elif user == 1:
        print("Its a draw")
    elif user == 2:
        print("You Win")
elif computer_choice == 2:
    if user == 0:
        print("You Win")
    elif user == 1:
        print("You Lose")
    elif user == 2:
        print("Its a draw")












