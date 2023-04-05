import random

# List of names for each category
OpeningBatsmans = ["Roshan", "Steve", "Satish", "Lingesh"]
MiddleOrder = ["Maddy", "Arun" ]
AllRounders = ["Dinesh","Sarathi","Kadal","Raghav"]
Hitters = ["Sathi","Bala"]
FastBowlersSwing = ["Ram","Retheesh"]
AllRounderPlus = ["Siva","Paul"]
True360 = ["Prakash","Saravanan"]

# Shuffle the names to create randomized teams
random.shuffle(OpeningBatsmans)
random.shuffle(MiddleOrder)
random.shuffle(AllRounders)
random.shuffle(Hitters)
random.shuffle(FastBowlersSwing)
random.shuffle(True360)
random.shuffle(AllRounderPlus)

# Split the shuffled names into two teams of equal size
team1 = OpeningBatsmans[:len(OpeningBatsmans)//2] + MiddleOrder[:len(MiddleOrder)//2] + AllRounders[:len(AllRounders)//2] + Hitters[:len(Hitters)//2] + FastBowlersSwing[:len(FastBowlersSwing)//2] + AllRounderPlus[:len(AllRounderPlus)//2] + True360[:len(True360)//2] 
team2 = OpeningBatsmans[len(OpeningBatsmans)//2:] + MiddleOrder[len(MiddleOrder)//2:] + AllRounders[len(AllRounders)//2:] + Hitters[len(Hitters)//2:] + FastBowlersSwing[len(FastBowlersSwing)//2:] + AllRounderPlus[len(AllRounderPlus)//2:] + True360[len(True360)//2:]

# Print the two teams
print("Team A:")
for name in team1:
    print(name)
    
print("\nTeam B:")
for name in team2:
    print(name)
