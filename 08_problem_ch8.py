#write a python function to print multiplicationtable of given number.

def multiply(n):
    for i in range(1,11):
        print(f"{n}*{i}={n*i}")
multiply(5)