import random
import time
delay = 5
close_time = time.time() + delay
while time.time()<close_time:
    n = random.randint(10000,99999)
    print(n)
    code = input("Enter Code: ")
    if int(code) == n :
        print("Left Reactor Stabilized - Further Breaches Detected: 2")
        n2 = random.randint(10000,99999)
        print(n2)
        code1 = input("Enter Code: ")
        if int(code1) == n2:
            print("Right Reactor Stabilized - Further Breaches Detected: 1")
            n3 = random.randint(10000,99999)
            print(n3)
            code2 = input("Enter Code: ")
            if int(code2) == n3:
                print("Middle Reactor Stabilized")
                print("Reactors Repaired")
                break
            else:
              print("Failed To Stabilize Reactors: Please Try Again")
            break    

        else:
         print("Failed To Stabilize Reactors: Please Try Again")
        break   
        
    else:
        print("Failed To Stabilize Reactors: Please Try Again")
        break

    