import random
number_1 = int(input('Enter first number'))
number_2 = int(input('Enter second number'))
def list_maker(lisname, userno):
    lisname = []
    while len(lisname) :
        number = random.randint(1, userno)
        if number not in lisname:
            lisname.append(number)
            lisname.sort()
            
list_maker('horiz', number_1)
list_maker('vert', number_2)




    