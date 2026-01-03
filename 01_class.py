# class Emloyee:
#     name="abhishek"
#     language="py"
#     salary="1200000"

# abhishek=Emloyee()
# print(abhishek.name,abhishek.language,abhishek.salary)


class Employee:
    language="python"    #this is class attribute
    salary=1200000

abhishek=Employee()
abhishek.name="ABHISHEK" #this is object attribute
print(abhishek.name,abhishek.language,abhishek.salary)

kumar=Employee()
kumar.name="KUMAR"
print(kumar.name,kumar.language,kumar.salary)

vishal=Employee()
vishal.name="VISHAL"
print(vishal.name,vishal.language,vishal.salary)

# here name is instance attributed and salary and language are classes attributes
#  as they directly belong to the class.
