import random
PasswordLength = int(input("Please Enter the Length of Password"))\
PasswordCharacter="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
Password = "".join(random.sample(PasswordCharacter,PasswordLength))
print(Password)