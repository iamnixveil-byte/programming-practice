Word = input("Enter some words \n")

def ReservedList (Word):
    Word = Word[: : -1 ]
    return Word
print(ReservedList(Word))