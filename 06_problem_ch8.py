#write a python function which converts inches to cms.
def inch_to_cms(inch):
    return inch*2.54

n=int(input("enter value in inches:"))

print(f"The corresponding value in cmsis{inch_to_cms(n)}")

