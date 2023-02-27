import random

lowercase="abcdefghijklmnopqrstuvwxyz"
uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="!@#$%^&*"
combn=list(lowercase+uppercase+numbers+symbols)
passlen=int(input("Enter the length of the password:"))
passwd="".join(random.sample(combn,passlen))
print("your randomly generated password is "+passwd)
