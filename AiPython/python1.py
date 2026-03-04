import random as rdm
import math

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [2,4,6,8,10,12,14,16,18,20]

weight = rdm.randint(0,1)
for i in range(100):
    guess = [weight * x for x in list1]

    checkGuess = [j - i for j,i in zip(list2,guess)]
    FinalGuess = [x ** 2 for x in checkGuess]
    for add in FinalGuess:
        add+=add
        AverageGuess = add/len(FinalGuess)
        error = weight - (0.01 *AverageGuess )
print(error)