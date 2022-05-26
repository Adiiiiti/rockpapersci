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
#Write your code below this line 👇
choice=int(input("what do you choose? type 0 for rock, 1 for paper ,2 for scissors"))
if(choice==0):
  print(rock)

elif(choice==1):
   print(paper)

else:
  print(scissors)
print("computer chose")
comp_ch=random.randint(0,2)
if(comp_ch==0):
  print(rock)

elif(comp_ch==1):
   print(paper)

else:
  print(scissors)

if(choice==comp_ch):
  print("DRAW")
elif(choice>comp_ch):
  print("YOU WIN")
else:
  print("YOU LOSE")