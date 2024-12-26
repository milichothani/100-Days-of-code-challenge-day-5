import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = [] #creating or we can say storing our generated password in a list
for alphabets in range(0, nr_letters):
    random_alphabet=random.choice(letters)
    password += random_alphabet

for num in range(0,nr_numbers  + 1):
    random_num =random.choice(numbers)
    password += random_num

for symb in range (0,nr_symbols + 1):
    random_symb = random.choice(symbols)
    password += random_symb
random.shuffle(password)
#then use shuffle function to shuffle the list items that is randomly chosen password elements
print(''.join(password))

