import random
import string
 #string is a module, not a function.    
pass_len = int(input("Enter the length of the password that you need:"))
charvalues = string.ascii_letters + string.digits + string.punctuation
#
password = ""
for i in range(pass_len):
    password += random.choice(charvalues)

print("Your",pass_len,"digit password is:", password)  
