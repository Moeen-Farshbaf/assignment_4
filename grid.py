n = int(input('enter width'))
m = int(input('enter lenght'))
def widthh():
    for i in range (0,n):
        if i%2==0:
            print("*", end='')
        else:
            print ('#',end='')
def width():
    for i in range (0,n):
        if i%2==0:
            print("#", end='')
        else:
            print ('*',end='')
        
for i in range (0,m):
    if i%2==0:
        widthh()
        print("")
    else:
        width()
        print('')
   
