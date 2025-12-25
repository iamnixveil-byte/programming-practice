Word = input("Enter some words \n")

def ReservedList (Word):
    Word = str(Word).split()
    Word = Word[: : -1 ]
    return Word
print(ReservedList(Word))