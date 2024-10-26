class A:
    def __init__(self,a):
        self.a = a
    def __lt__(self,other):
        if(self.a<other.a):
            return "Object1 is less than Object2"
        else:
            return "Object2 is less than Object1"
    def __eq__(self,other):
        if(self.a==other.a):
            return "Object1 i equal to Object2"
        else:
            return"Object1 is not equal to Object2"
obj1 = A(12)
obj2 = A(21)
print("Passed values are: ", obj1.a,obj2.a)
print(obj1<obj2)

obj3 = A(5)
obj4 = A(5)
print("Passed values are: ", obj3.a,obj4.a)
print(obj3==obj4)
