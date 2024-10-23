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
import random

user=int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
if user==0:
    print(rock)
elif user==1:
    print(paper)
elif user==2:
    print(scissors)

print("Computer chose: ")
computer=random.randint(0,2)
# print(computer)
if computer==0:
    print(rock)
elif computer==1:
    print(paper)
else:
    print(scissors)


if (user==0 and computer==0 )or (user==1 and computer==1) or (user==2 and computer==2) :
    print('It\'s a draw')
elif (user==0 and computer==2)or (user==1 and computer==0) or (user==2 and computer==1):
    print("You won")
else:
    print("You loose")
