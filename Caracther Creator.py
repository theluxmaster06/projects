race_list = ["human", "elf", "dwarf", "tiefling", "aasimar", "dragonborn", "gnome", "halfling", "goliath", "orc", "skip"]

print("-----DnD Caracther Creator-----")
print("choose a race")

for race in race_list:
    print(race)

print("--------------------------------")
selected = False

while selected == False:

    race_choice = input("What race would you like to play: ").lower()
    if race_choice in race_list:
        print("You have chosen", race_choice)
        selected = True
    else:
        print("You have to choose a valid race.")

class_list = ["barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rogue", "sorcerer", "warlock", "wizard", "skip"]

print("-----DnD Caracther Creator-----")
print("choose a class")

for clas in class_list:
    print(clas)


    selected = False
print("--------------------------------")

while selected == False:

    class_choice = input("What class would you like to play: ").lower()
    if class_choice in class_list:
        print("You have chosen", class_choice)
        selected = True
    else:
        print("You have to choose a valid class.")

print("race:", race_choice)
print("class", class_choice)

print ("---{class_choice}---")


# stat point buy calculator
print("time to choose your stats")

point = 27
stats = {
    "strength": 8,
    "dexterity": 8,
    "constitution": 8,
    "intelligence": 8,
    "wisdom": 8,
    "charisma": 8
}

print("you have", point, "points to spend")
for stat, value in stats.items():
    print(stat, ":", value)
while point > 0:
    stat_choice = input("which stat do you want to increase: ").lower()
    if stat_choice in stats:
        increase = int(input("how much do you want to increase it by (1-5): "))
        if increase < 1 or increase > 5:
            print("you can only increase a stat by 1-5 points at a time")
        elif stats[stat_choice] + increase > 15:
            print("you can only increase a stat to a maximum of 15")
        elif point - increase < 0:
            print("you don't have enough points to do that")
        else:
            stats[stat_choice] += increase
            point -= increase
            print(stat_choice, "has been increased to", stats[stat_choice])
            print("you have", point, "points left to spend")
    else:
        print("that is not a valid stat")
print("you have spent all your points")
for stat, value in stats.items():
    print(stat, ":", value) 


# stat bonus for races
if race_choice == "human":
    stats["strength"] += 1
    stats["dexterity"] += 1
    stats["constitution"] += 1
    stats["intelligence"] += 1
    stats["wisdom"] += 1
    stats["charisma"] += 1
    print("as a human you get +1 to all stats")
    for stat, value in stats.items():
        print(stat, ":", value)     

elif race_choice == "elf":
    stats["dexterity"] += 2
    stats["intelligence"] += 1
    print("as an elf you get +2 dexterity and +1 intelligence")
    for stat, value in stats.items():
        print(stat, ":", value) 

elif race_choice == "dwarf":
    stats["constitution"] += 2
    stats["wisdom"] += 1
    print("as a dwarf you get +2 constitution and +1 wisdom")
    for stat, value in stats.items():
        print(stat, ":", value) 

elif race_choice == "tiefling":
    stats["intelligence"] += 1
    stats["charisma"] += 2
    print("as a tiefling you get +1 intelligence and +2 charisma")
    for stat, value in stats.items():
        print(stat, ":", value) 

elif race_choice == "aasimar":
    stats["wisdom"] += 1
    stats["charisma"] += 2
    print("as an aasimar you get +1 wisdom and +2 charisma")
    for stat, value in stats.items():
        print(stat, ":", value) 

elif race_choice == "dragonborn":
    stats["strength"] += 2
    stats["charisma"] += 1
    print("as a dragonborn you get +2 strength and +1 charisma")
    for stat, value in stats.items():
        print(stat, ":", value) 

elif race_choice == "gnome":
    stats["intelligence"] += 2
    stats["dexterity"] += 1
    print("as a gnome you get +2 intelligence and +1 dexterity")
    for stat, value in stats.items():
        print(stat, ":", value)

elif race_choice == "halfling":
    stats["dexterity"] += 2
    stats["charisma"] += 1
    print("as a halfling you get +2 dexterity and +1 charisma")
    for stat, value in stats.items():
        print(stat, ":", value)

elif race_choice == "goliath":
    stats["strength"] += 2
    stats["constitution"] += 1
    print("as a goliath you get +2 strength and +1 constitution")
    for stat, value in stats.items():
        print(stat, ":", value)

elif race_choice == "orc":
    stats["strength"] += 2
    stats["constitution"] += 1
    print("as an orc you get +2 strength and +1 constitution")
    for stat, value in stats.items():
        print(stat, ":", value)

else:
    print("ur race does not have any stat bonuses")


# hitpoint calculator based on class
if class_choice == "barbarian":
    hit_points = 12 + (stats["constitution"] - 10) // 2
    # based on wiki dot 5e this is how u calculate hitpoints
    print("as a barbarian you have", hit_points, "hit points")



elif class_choice == "bard":
    hit_points = 8 + (stats["constitution"] - 10) // 2
    print("as a bard you have", hit_points, "hit points")   

elif class_choice == "cleric":
    hit_points = 8 + (stats["constitution"] - 10) // 2
    print("as a cleric you have", hit_points, "hit points")

elif class_choice == "druid":
    hit_points = 8 + (stats["constitution"] - 10) // 2
    print("as a druid you have", hit_points, "hit points")  

elif class_choice == "fighter":
    hit_points = 10 + (stats["constitution"] - 10) // 2
    print("as a fighter you have", hit_points, "hit points")

elif class_choice == "monk":
    hit_points = 8 + (stats["constitution"] - 10) // 2
    print("as a monk you have", hit_points, "hit points")   

elif class_choice == "paladin":
    hit_points = 10 + (stats["constitution"] - 10) // 2
    print("as a paladin you have", hit_points, "hit points")       

elif class_choice == "ranger":
    hit_points = 10 + (stats["constitution"] - 10) // 2
    print("as a ranger you have", hit_points, "hit points") 

elif class_choice == "rogue":
    hit_points = 8 + (stats["constitution"] - 10) // 2
    print("as a rogue you have", hit_points, "hit points")  

elif class_choice == "sorcerer":
    hit_points = 6 + (stats["constitution"] - 10) // 2
    print("as a sorcerer you have", hit_points, "hit points")

elif class_choice == "warlock":
    hit_points = 8 + (stats["constitution"] - 10) // 2
    print("as a warlock you have", hit_points, "hit points")

elif class_choice == "wizard":
    hit_points = 6 + (stats["constitution"] - 10) // 2
    print("as a wizard you have", hit_points, "hit points")

else:
    print("ur class does not have any hit points")


# quick caracther summary so u dont get overwhelemed

print( )
print( )
print("-----Caracther Summary-----")
print( )
print( )

print ("race", race_choice)
print ("class", class_choice)
print ("stats", stats)
print ("hit points", hit_points)
print( )
print("-----End of Summary-----")

print("time to choose your equipment")

if class_choice == "barbarian":
    print("as a barbarian you can choose between a greataxe or any martial melee weapon")
    print("you can also choose between two handaxes or any simple weapon")
    print("you also get an explorer's pack and four javelins")
    weapon_choice = input("which weapon do you want: ").lower()
    if weapon_choice == "greataxe":
        print("you have chosen a greataxe")
    else:
        print("you have chosen a", weapon_choice)
    simple_weapon_choice = input("which simple weapon do you want: ").lower()
    if simple_weapon_choice == "handaxes":
        print("you have chosen two handaxes")
    else:
        print("you have chosen a", simple_weapon_choice)
    print("you also get an explorer's pack and four javelins")

if class_choice == "bard":
    print("as a bard you can choose")

else:
    print("equipment for this class is not yet implemented")
