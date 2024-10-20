class Jermanshepherd:
    species = "Dog"
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
drew = Jermanshepherd("Drew", 10)
fru = Jermanshepherd("Fru", 15)

print("Drew is a {}".format(drew.species))
print("Fru is a {}".format(fru.species))

print("{} is {} years old".format(drew.name,drew.age))
print("{} is {} years old".format(fru.name,fru.age))