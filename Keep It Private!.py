class creation:
    __privateVar = 5
    def __privateMath(self):
        print("I am inside the class")
        
    def hello(self):
        print("Private variable value is: ",creation.__privateVar)
fool = creation()
fool.hello()
fool.__privateMath