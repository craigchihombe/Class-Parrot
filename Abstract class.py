from abc import ABC, abstractmethod

class ABsclass(ABC):
    
    def print(self,x):
        print("Passed value",x)
        
    def task(self):
        print("We are in ABsclass")
class Test_class(ABsclass):
    def task(self):
        print("We are in Test class")
        
test_obj = Test_class()
test_obj.task()
test_obj.print(598)