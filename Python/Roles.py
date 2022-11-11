import random 

chars = "123456789"

while 1:
    len = int("7")
    count = int("1")
    for x in range(0,count):
        password = ""
        for x in range(0,len):
            pass_chars = random.choice(chars)
            print(pass_chars)