import random
change = 0
keep = 0

numberOfExperiment = 10000

for i in range(0,numberOfExperiment):
    print("Experiment number " + str(i+1))
    prizes = ["goat","goat","car"]
    doors = []
    
    while(len(prizes)>0):
        prizeNumber = random.randint(0,len(prizes)-1)
        prize = prizes.pop(prizeNumber)
        doors.append(prize)
        
    print(doors)
    choice = random.randint(0,2)
    print("You chose door number " + str(choice+1))

    changeOrKeep = random.randint(0,1)
    
    if (changeOrKeep == 0):
        while True:
            randomDoor = random.randint(0,2)
            if (doors[randomDoor] != "car" and choice != randomDoor):
                break
        print("Changing....")
        while True:
            doorToChange = random.randint(0,2)
            if (doorToChange != randomDoor and doorToChange != choice):
                break
        choice = doorToChange
        if (doors[choice] == "car"):
            change+=1
            print("Changing worked!")
            print("****************")
        else:
            keep+=1
            print("Changing did not work! Keeping would work!")
            print("******************************************")
    elif (changeOrKeep==1):
        print("Keeping....")
        if (doors[choice] == "car"):
            keep+=1
            print("Keeping worked!")
            print("***************")
        else:
            change+=1
            print("Keeeping did not work! Changing would work!")
            print("*******************************************")
        
print("Probability of winning for changing strategy " + str(change/numberOfExperiment))
print("Probability of winning for keeping strategy " + str(keep/numberOfExperiment))
        
            
    