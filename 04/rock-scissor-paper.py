# Rock 1 - Paper 2 - Scissor 3
# random module -> randint(1, 3)

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
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to Rock Paper Scissor Game vs Computer!")

user_choice = input("""Select:
[1] Rock
[2] Paper
[3] Scissor
:: """)

computer_choice = random.randint(1, 3)
computer = str(computer_choice)

# checking data type
# print(f"You: {user_choice} / Computer: {computer}")
# print(type(user_choice))
# print(type(computer))

# if user 1 (Rock) and comp 1 (Rock) -> game tie
# user 1 rock and comp 2 (Paper) -> user lose
# user 1 rock and comp 3 scissor -> user win

# user 2 paper and comp 1 rock -> user win
# user 2 paper and comp 2 paper -> game tie
# user 2 paper and comp 3 scissor -> user lose

# user 3 scissor and comp 1 rock -> user lose
# user 3 scissor and comp 2 paper -> user win
# user 3 scissor and comp 3 scissor -> game tie

if user_choice == "1" and computer == "1":
    print(rock)
    print("The Game Tie - both choose Rock")
    print(rock)
elif user_choice == "1" and computer == "2":
    print(rock)
    print("You Lose! Computer choose Paper")
    print(paper)
elif user_choice == "1" and computer == "3":
    print(rock)
    print("You Win! Rock beat Scissor")
    print(scissor)
elif user_choice == "2" and computer == "1":
    print(paper)
    print("You Win! Paper beat Rock")
    print(rock)
elif user_choice == "2" and computer == "2":
    print(paper)
    print("The Game Tie! Both choose Paper")
    print(paper)
elif user_choice == "2" and computer == "3":
    print(paper)
    print("You Lose! Computer choose Scissor")
    print(scissor)
elif user_choice == "3" and computer == "1":
    print(scissor)
    print("You Lose! Computer choose Rock")
    print(rock)
elif user_choice == "3" and computer == "2":
    print(scissor)
    print("You Win! Scissor beat Paper")
    print(paper)
elif user_choice == "3" and computer == "3":
    print(scissor)
    print("The Game Tie! Both choose Scissor")
    print(scissor)

