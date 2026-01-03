class Employee:
    language="python"
    salary = 1200000

    def __init__(self):
        print("i am creating an object")

    def getinfo(self):
        print(f"the language is {self.language}.the salary is {self.salary}")


    @staticmethod
    def greet():
        print("good morning")



Abhishek=Employee()
Abhishek.name="Abhishek"
print(Abhishek.name,Abhishek.salary)
Abhishek.getinfo()


