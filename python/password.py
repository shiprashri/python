#Password Generator Project
while(True):
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    a= int(input("How many letters would you like in your password?\n")) 
    b = int(input(f"How many symbols would you like?\n"))
    c = int(input(f"How many numbers would you like?\n"))
    password = [ ]
    for i in range (0,a):
      password.append(random.choice(letters))
    for j in range (0,b):
      password += random.choice(numbers)
    for k in range (0,c):
      password += random.choice(symbols)
    print(password)
    random.shuffle(password)
    print(password)

    password_1 = " "
    for i in password :
      password_1 +=  i
    print(f"Your password is {password_1}")
