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

#Write your code below this line 👇
import random

choices = [rock, paper, scissors]

player = input("Choose between Rock (0), Paper(1), Scissors(2)")
player = int(player)

computer = random.randint(0,2)

print(player)
print(choices[player])
print(computer)
print(choices[computer])

if player == 0 and computer==1:
  print("You lose")
elif player == computer:
  print("draw")
elif player ==0 and computer ==2:
  print("you win")
elif player == 1 and computer == 0:
  print("you win ")
elif player == 1 and computer == 2:
  print("You lose")
elif player == 2 and computer == 0:
  print("You lose")
elif player == 2 and computer == 1:
  print("you win ")
  
