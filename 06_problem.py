#create an empty dictionary.allow 4 friends to enter their favorite language as value 
#and use key as their names.Assume that the names are unique.
s={}

name=input("enter friends name :-")
lang=input("enter language name:-")
s.update({name:lang})
name=input("enter friends name :-")
lang=input("enter language name:-")
s.update({name:lang})
name=input("enter friends name :-")
lang=input("enter language name:-")
s.update({name:lang})
name=input("enter friends name :-")
lang=input("enter language name:-")
s.update({name:lang})

print(s)

# problem 7 #if the names of two friends are same ;what will happen to the program in problem 6?
# problem 8 #if languages of two friends are same ;what will happen to the program in problem 6?
