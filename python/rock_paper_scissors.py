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
while (True):
 a = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
 computer_choice = random.randint(0,2)
 if a > 2 or a < 0:
   print("You typed an invalid number , you lose!")
 elif a == 0:
   print(rock)
   if computer_choice == 0:
     print(f"Computer chose: \n {rock} \n It's a draw ")
   elif computer_choice == 1:
     print(f"Computer chose : \n {paper} \n You loss")
   else :
     print(f"Computer chose : \n {scissors} \n You win")
 elif a == 1:
   print(paper)
   if computer_choice == 0:
     print(f"Computer chose: \n {rock} \n You win")
   elif computer_choice == 1:
     print(f"Computer chose : \n {paper} \n Its a draw")
   else :
     print(f"Computer chose : \n {scissors} \n You loss")
 else :
   print(scissors)
   if computer_choice == 0:
     print(f"Computer chose: \n {rock} \n You loss")
   elif computer_choice == 1:
     print(f"Computer chose : \n {paper} \n You win")
   else :
     print(f"Computer chose : \n {scissors} \n It's a draw")
