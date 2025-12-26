# write a python program using functions to convert celsius to fahrenheit.
#c/5=(f-32)/9     # formula

def f_to_c(f):
    return 5*(f-32)/9
f = int(input("enter temperature in f"))
c=f_to_c(f)
print(f"{round(c,2)}°c")