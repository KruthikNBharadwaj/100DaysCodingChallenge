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

#Write your code below this line 👇
game_img=[rock,paper,scissors]
user=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user>=3 or user<0:
  print("Invalid")
else:
  print(game_img[user])
  comp_choice=random.randint(0,2)
  print("Computer chose:")
  print(game_img[comp_choice])
  if user==0 and comp_choice==2:
    print("You win")
  elif comp_choice>user:
    print("You lose")
  elif comp_choice==user:
    print("Draw")
  elif comp_choice==0 and user==2:
    print("You lose")
  elif comp_choice==0 and user==1:
    print("You win")