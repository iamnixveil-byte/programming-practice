list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [2,4,6,8,10,12,14,16,18,20]

weight = int(input("enter any number"))

guess = [weight * x for x in list1]


print(guess)