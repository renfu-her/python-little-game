import random
import datetime

ALP = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I",
    "J", "K", "L", "M", "N", "O", "P", "Q", "R",
    "S", "T", "V", "W", "X", "Y", "Z"
]

r = random.choice(ALP)

alp = ""

for i in ALP:
    if i != r:
        alp += i

print(alp)

st = datetime.datetime.now()
ans = input("Enter the missing letter: ")

if ans == r:
    print("Correct!")
    et = datetime.datetime.now()
    print("Time taken: ", et - st)
else:
    print("Wrong!")
    print("The correct answer is: ", r)
