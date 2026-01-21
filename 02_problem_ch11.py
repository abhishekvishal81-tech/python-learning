#Create a class'Pets'from a class 'Animals' and further create a class'Dog' from 'Pets'.Add a method 'Bark' to class 'Dog'.
class Animals:
    pass
class Pets(Animals):
    pass
class Dogs(Pets):
    @staticmethod
    def Bark():
        print("Bow Bow")

d=Dogs()
d.Bark()