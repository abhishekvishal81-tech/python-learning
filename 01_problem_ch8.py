#write a program using functions to find the greatest of three numbers.
a = int(input(("enter a")))
b = int(input(("enter b")))
c = int(input(("enter c")))

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    

print("Greatest number is:", greatest(a, b, c))
