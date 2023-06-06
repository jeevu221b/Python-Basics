a = 100
isPrime = True
if a<=1:
    print("Invalid number")
else:
    if a == 2:
        print("Prime")
    else:
        for i in range(2, a):
            if a%i == 0:
                isPrime = False
                break
    if isPrime:
        print("Prime")
    else:
        print("Composite")

            


    






       
