#create class
class IOString():
    #constructor to set default value
    def __init__(self):
        self.str1 = " "
        
        #function to get input from the user
    def get_String(self):
        self.str1 = input("Enter the string: ")
    
    #function to print the string in upper case
    def print_String(self):
        print("The result is : ", self.str1.upper())
        
#object creation
str1 = IOString()

#call functions
str1.get_String()
str1.print_String()