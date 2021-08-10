n = int(input('enter width'))
m = int(input('enter lenght'))
def width():
    for i in range (0,n):
        if i%2>0:
            print("*", end='')
        else:
            print ('#',end='')
        
for i in range (0,m):
    width()
    print('')
