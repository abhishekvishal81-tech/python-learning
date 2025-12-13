a=31

t = type(a) #class<int>
print(t)

a=31.2

t = type(a) #class<float>
print(t)

a="abhishek"

t = type(a) #class<string>
print(t)

a="31.09"

t = type(a) #class<string becaouse double quotes me kuch v ho string mana jayega>
print(t)


a="31.2"
b=float(a) #a but the type should be float

t = type(b) #class<int>
print(t)



#str(31)=>"31" #integer to string conversion
#int(32)=>32 #string to integer conversion
#float(32)=> integer to float conversion