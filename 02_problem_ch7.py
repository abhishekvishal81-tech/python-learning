# write a program to greet all the person names stored in a list'l' and which starts with S.
#l=["abhishek","kumar","singh","sohan"]
l=["abhishek","kumar","singh","sohan"]

for name in l:
    if(name.startswith("s")):
        print(f"hello {name}")