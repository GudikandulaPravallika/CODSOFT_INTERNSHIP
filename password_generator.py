import string
import random
length=int(input("enter desired length of pasword"))
complexity_type=input("enter type of complexity like :\n1.easy\n2.hard")
characters=""

if(complexity_type == "easy".casefold()):
    characters+=string.ascii_letters+string.digits
elif(complexity_type == "hard".casefold()):
    characters+=string.ascii_letters+string.punctuation+string.digits+string.punctuation
else:
    print("Invalid choice")
password=""
for i in range(length):
    pwd=random.choice(characters)
    password+=pwd
print("Generated password is:",password)


    