class Flashcard:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word + '('+self.meaning+')'
flash = []
print("Welcome to Flashcard application")

while(True):
    word = input("Enter the name you want to add to the Flashcard: ")
    meaning = input("Enter the meaning of the word you entered: ")
    flash.append(Flashcard(word,meaning))
    option = int(input("Enter 0 , if you want to add another Flashcard otherwise enter 1: "))
    if(option):
        break
print("Your Flashcard")
for i in flash:
    print(">",i)  