#create class
class Employee:
    #initializing
    def __init__(self):
        print("Empolyee created")
        
    #calling destructor
    def __del__(self):
        print("Destructor called")
        
#create object
def Create_obj():
    print("Making object...")
    
    obj = Employee()
    print("Function End...")
    
    return obj

print("Calling create object function")
obj = Create_obj()
print("Your programme ends here...")