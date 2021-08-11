active = True
factoriels = []


def factorielchecker(n, check):   
        for i in range (0,n):
            no = (i*(i+1))
            factoriels.append(no)
        if check in factoriels:
            print ("Yes")
        else:
            print ('no')
while active:
    n = int(input("Please enter the range you want to observe:"))
    check = int(input("Now enter the number:"))

    factorielchecker(n, check)
    will = input("Are we done?()yes/no")
    if will == "no":
        pass
    if will =="yes":
        active = False
        print ("Have a nice day.")