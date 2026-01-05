# create a class"programmer" for storing information of few programmers working at Microsoft


class Programmer:
    company="Microsoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin

P=Programmer("Abhishek",1200000,834001)
print(P.company,P.name,P.salary,P.pin)

P=Programmer("Kumar",1300000,834002)
print(P.company,P.name,P.salary,P.pin)

P=Programmer("Vishal",1400000,834003)
print(P.company,P.name,P.salary,P.pin)