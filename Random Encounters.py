import random

with open("RandomEncounters.txt", 'r') as fin:
    fin_arr = []
    for line in fin:
        if line != "\n":
            fin_arr.append(line)
    choice = ""
    while choice == "":
        choice = random.choice(fin_arr)
    print(choice)

input()