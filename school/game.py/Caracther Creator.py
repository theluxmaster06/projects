import json
#-----------[race selection]-----------------

race_list = ["human", "elf", "dwarf", "tiefling", "aasimar", "dragonborn", "gnome", "halfling", "goliath", "orc", "skip"]

print("-----DnD Caracther Creator-----")
print("choose a race")

for race in race_list:
    print(race.capitalize())

print("--------------------------------")
selected = False

while selected == False:

    race_choice = input("What race would you like to play: ").lower().strip()
    if race_choice in race_list:
        print("You have chosen", race_choice.capitalize())
        selected = True
    else:
        print("You have to choose a valid race.")

#-----------[class selection]-----------------

class_list = ["barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rogue", "sorcerer", "warlock", "wizard", "skip"]

print("-----DnD Caracther Creator-----")
print("choose a class")

for clas in class_list:
    print(clas)


    selected = False
print("--------------------------------")

while selected == False:

    class_choice = input("What class would you like to play: ").lower().strip()
    if class_choice in class_list:
        print("You have chosen", class_choice.capitalize())
        selected = True
    else:
        print("You have to choose a valid class.")

print("race:", race_choice)
print("class", class_choice)

print("---{race_choice}---")

#-----------[stat allocation]-----------------

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
print("you can increase a stat by 1-5 points at a time")
print("you can only increase a stat to a maximum of 15")
for stat, value in stats.items():
    print(stat, ":", value)
print("---------------------------------------")
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
            print(f"{stat_choice}has been increased to {stats[stat_choice]}")
            print(f"you have {point} points left to spend")
    else:
        print("that is not a valid stat")
print("you have spent all your points")

#---------------------------------------------

print("time to apply racial stat bonuses")

#-----------[racial stat bonuses]-----------------

if race_choice == "human":
    stats["strength"] += 1
    stats["dexterity"] += 1
    stats["constitution"] += 1
    stats["intelligence"] += 1
    stats["wisdom"] += 1
    stats["charisma"] += 1
    print("as a human you get +1 to all stats")

#---------------------------------------------

elif race_choice == "elf":
    stats["dexterity"] += 2
    stats["intelligence"] += 1
    print("as an elf you get +2 dexterity and +1 intelligence")

#---------------------------------------------

elif race_choice == "dwarf":
    stats["constitution"] += 2
    stats["wisdom"] += 1
    print("as a dwarf you get +2 constitution and +1 wisdom")

#---------------------------------------------

elif race_choice == "tiefling":
    stats["intelligence"] += 1
    stats["charisma"] += 2
    print("as a tiefling you get +1 intelligence and +2 charisma")

#---------------------------------------------

elif race_choice == "aasimar":
    stats["wisdom"] += 1
    stats["charisma"] += 2
    print("as an aasimar you get +1 wisdom and +2 charisma")

#---------------------------------------------

elif race_choice == "dragonborn":
    stats["strength"] += 2
    stats["charisma"] += 1
    print("as a dragonborn you get +2 strength and +1 charisma")

#---------------------------------------------

elif race_choice == "gnome":
    stats["intelligence"] += 2
    stats["dexterity"] += 1
    print("as a gnome you get +2 intelligence and +1 dexterity")

#---------------------------------------------    

elif race_choice == "halfling":
    stats["dexterity"] += 2
    stats["charisma"] += 1
    print("as a halfling you get +2 dexterity and +1 charisma")

#---------------------------------------------

elif race_choice == "goliath":
    stats["strength"] += 2
    stats["constitution"] += 1
    print("as a goliath you get +2 strength and +1 constitution")

#---------------------------------------------

elif race_choice == "orc":
    stats["strength"] += 2
    stats["constitution"] += 1
    print("as an orc you get +2 strength and +1 constitution")

#---------------------------------------------

else:
    print("ur race does not have any stat bonuses")

for stat, value in stats.items():
        print(stat, ":", value)

print( )
print("---------------------------------------")
# -------------[hitpoints]-----------------
print("time to calculate your hit points")

if class_choice == "barbarian":
    hit_points = 12 + (stats["constitution"] - 10) // 2
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

#------------------------------------------------------------------------------------

elif class_choice == "bard":
    print("as a bard you can choose between a rapier, a longsword, or any simple weapon")
    print("you also get a diplomat's pack or an entertainer's pack")
    print("you also get a lute and leather armor and a dagger")
    weapon_choice = input("which weapon do you want: ").lower()
    if weapon_choice == "rapier":
        print("you have chosen a rapier")
    elif weapon_choice == "longsword":
        print("you have chosen a longsword")
    else:
        print("you have chosen a", weapon_choice)
    pack_choice = input("which pack do you want: ").lower()
    if pack_choice == "diplomat's pack":
        print("you have chosen a diplomat's pack")
    elif pack_choice == "entertainer's pack":
        print("you have chosen an entertainer's pack")
    else:
        print("you have chosen a", pack_choice)
    print("you also get a lute, leather armor, and a dagger")

#------------------------------------------------------------------------------------

elif class_choice == "cleric":
    print("as a cleric you can choose between a mace or a warhammer (if proficient)")
    print("you can also choose between scale mail, leather armor, or chain mail (if proficient)")
    print("you also get a light crossbow and 20 bolts or any simple weapon")
    print("you also get a priest's pack or an explorer's pack")
    print("you also get a shield and a holy symbol")
    weapon_choice = input("which weapon do you want: ").lower()
    if weapon_choice == "mace":
        print("you have chosen a mace")
    elif weapon_choice == "warhammer":
        print("you have chosen a warhammer")
    else:
        print("you have chosen a", weapon_choice)
    armor_choice = input("which armor do you want: ").lower()
    if armor_choice == "scale mail":
        print("you have chosen scale mail")
    elif armor_choice == "leather armor":
        print("you have chosen leather armor")
    elif armor_choice == "chain mail":
        print("you have chosen chain mail")
    else:
        print("you have chosen", armor_choice)
    ranged_weapon_choice = input("which ranged weapon do you want: ").lower()
    if ranged_weapon_choice == "light crossbow":
        print("you have chosen a light crossbow and 20 bolts")
    else:
        print("you have chosen a", ranged_weapon_choice)
    pack_choice = input("which pack do you want: ").lower()
    if pack_choice == "priest's pack":
        print("you have chosen a priest's pack")
    elif pack_choice == "explorer's pack":
        print("you have chosen an explorer's pack")
    else:
        print("you have chosen a", pack_choice)
    print("you also get a shield and a holy symbol")

#------------------------------------------------------------------------------------

elif class_choice == "druid":
    print("as a druid you can choose between a wooden shield or any simple weapon")
    print("you also get a scimitar or any simple melee weapon")
    print("you also get leather armor, an explorer's pack, and a druidic focus")
    weapon_choice = input("which weapon do you want: ").lower()
    if weapon_choice == "wooden shield":
        print("you have chosen a wooden shield")
    else:
        print("you have chosen a", weapon_choice)
    melee_weapon_choice = input("which melee weapon do you want: ").lower()
    if melee_weapon_choice == "scimitar":
        print("you have chosen a scimitar")
    else:
        print("you have chosen a", melee_weapon_choice)
    print("you also get leather armor, an explorer's pack, and a druidic focus")

#------------------------------------------------------------------------------------

elif class_choice == "fighter":
    print("as a fighter you can choose between a chain mail or leather armor, longbow, and 20 arrows")
    print("you can also choose between a martial weapon and a shield or two martial weapons")
    print("you also get a light crossbow and 20 bolts or two handaxes")
    print("you also get a dungeoneer's pack or an explorer's pack")
    armor_choice = input("which armor do you want: ").lower()
    if armor_choice == "chain mail":
        print("you have chosen chain mail")
    elif armor_choice == "leather armor":
        print("you have chosen leather armor, a longbow, and 20 arrows")
    else:
        print("you have chosen", armor_choice)
    weapon_choice = input("which weapon do you want: ").lower()
    if weapon_choice == "martial weapon and a shield":
        print("you have chosen a martial weapon and a shield")
    elif weapon_choice == "two martial weapons":
        print("you have chosen two martial weapons")
    else:
        print("you have chosen", weapon_choice)
    ranged_weapon_choice = input("which ranged weapon do you want: ").lower()
    if ranged_weapon_choice == "light crossbow":
        print("you have chosen a light crossbow and 20 bolts")
    elif ranged_weapon_choice == "two handaxes":
        print("you have chosen two handaxes")
    else:
        print("you have chosen", ranged_weapon_choice)
    pack_choice = input("which pack do you want: ").lower()
    if pack_choice == "dungeoneer's pack":
        print("you have chosen a dungeoneer's pack")
    elif pack_choice == "explorer's pack":
        print("you have chosen an explorer's pack")
    else:
        print("you have chosen a", pack_choice)

#------------------------------------------------------------------------------------

elif class_choice == "monk":
    print("as a monk you can choose between a shortsword or any simple weapon")
    print("you also get a dungeoneer's pack or an explorer's pack")
    print("you also get 10 darts")
    weapon_choice = input("which weapon do you want: ").lower()
    if weapon_choice == "shortsword":
        print("you have chosen a shortsword")
    else:
        print("you have chosen a", weapon_choice)
    pack_choice = input("which pack do you want: ").lower()
    if pack_choice == "dungeoneer's pack":
        print("you have chosen a dungeoneer's pack")
    elif pack_choice == "explorer's pack":
        print("you have chosen an explorer's pack")
    else:
        print("you have chosen a", pack_choice)
    print("you also get 10 darts")

#------------------------------------------------------------------------------------

elif class_choice == "paladin":
    print("as a paladin you can choose between a martial weapon and a shield or two martial weapons")
    print("you also get five javelins")
    print("you also get an explorer's pack and chain mail")
    weapon_choice = input("which weapon do you want: ").lower()
    if weapon_choice == "martial weapon and a shield":
        print("you have chosen a martial weapon and a shield")
    elif weapon_choice == "two martial weapons":
        print("you have chosen two martial weapons")
    else:
        print("you have chosen", weapon_choice)
    print("you also get five javelins, an explorer's pack, and chain mail")

#------------------------------------------------------------------------------------

elif class_choice == "ranger":
    print("as a ranger you can choose between scale mail or leather armor, a longbow, and 20 arrows")
    print("you can also choose between a martial weapon and a shield or two martial weapons")
    print("you also get a dungeoneer's pack or an explorer's pack")
    weapon_choice = input("which weapon do you want: ").lower()
    if weapon_choice == "martial weapon and a shield":
        print("you have chosen a martial weapon and a shield")
    elif weapon_choice == "two martial weapons":
        print("you have chosen two martial weapons")
    else:
        print("you have chosen", weapon_choice)
    armor_choice = input("which armor do you want: ").lower()
    if armor_choice == "scale mail":
        print("you have chosen scale mail")
    elif armor_choice == "leather armor":
        print("you have chosen leather armor, a longbow, and 20 arrows")
    else:
        print("you have chosen", armor_choice)
    pack_choice = input("which pack do you want: ").lower()
    if pack_choice == "dungeoneer's pack":
        print("you have chosen a dungeoneer's pack")
    elif pack_choice == "explorer's pack":
        print("you have chosen an explorer's pack")
    else:
        print("you have chosen a", pack_choice)

#------------------------------------------------------------------------------------

elif class_choice == "rogue":
    print("as a rogue you can choose between a rapier, a shortsword, or any simple weapon")
    print("you also get a burglar's pack, a dungeoneer's pack, or an explorer's pack")
    print("you also get leather armor, two daggers, and thieves' tools")
    weapon_choice = input("which weapon do you want: ").lower()
    if weapon_choice == "rapier":
        print("you have chosen a rapier")
    elif weapon_choice == "shortsword":
        print("you have chosen a shortsword")
    else:
        print("you have chosen a", weapon_choice)
    pack_choice = input("which pack do you want: ").lower()
    if pack_choice == "burglar's pack":
        print("you have chosen a burglar's pack")
    elif pack_choice == "dungeoneer's pack":
        print("you have chosen a dungeoneer's pack")
    elif pack_choice == "explorer's pack":
        print("you have chosen an explorer's pack")
    else:
        print("you have chosen a", pack_choice)
    print("you also get leather armor, two daggers, and thieves' tools")

#------------------------------------------------------------------------------------

elif class_choice == "sorcerer":
    print("as a sorcerer you can choose between a light crossbow and 20 bolts or any simple weapon")
    print("you also get a component pouch or an arcane focus")
    print("you also get two daggers")
    weapon_choice = input("which weapon do you want: ").lower()
    if weapon_choice == "light crossbow":
        print("you have chosen a light crossbow and 20 bolts")
    else:
        print("you have chosen a", weapon_choice)
    focus_choice = input("which focus do you want: ").lower()
    if focus_choice == "component pouch":
        print("you have chosen a component pouch")
    elif focus_choice == "arcane focus":
        print("you have chosen an arcane focus")
    else:
        print("you have chosen a", focus_choice)
    print("you also get two daggers")

#------------------------------------------------------------------------------------

elif class_choice == "warlock":
    print("as a warlock you can choose between a light crossbow and 20 bolts or any simple weapon")
    print("you also get a component pouch or an arcane focus")
    print("you also get leather armor, any simple weapon, and two daggers")
    weapon_choice = input("which weapon do you want: ").lower()
    if weapon_choice == "light crossbow":
        print("you have chosen a light crossbow and 20 bolts")
    else:
        print("you have chosen a", weapon_choice)
    focus_choice = input("which focus do you want: ").lower()
    if focus_choice == "component pouch":
        print("you have chosen a component pouch")
    elif focus_choice == "arcane focus":
        print("you have chosen an arcane focus")
    else:
        print("you have chosen a", focus_choice)
    print("you also get leather armor, any simple weapon, and two daggers")

#------------------------------------------------------------------------------------

elif class_choice == "wizard":
    print("as a wizard you can choose between a quarterstaff or a dagger")
    print("you also get a component pouch or an arcane focus")
    print("you also get a scholar's pack or an explorer's pack")
    print("you also get a spellbook")
    weapon_choice = input("which weapon do you want: ").lower()
    if weapon_choice == "quarterstaff":
        print("you have chosen a quarterstaff")
    elif weapon_choice == "dagger":
        print("you have chosen a dagger")
    else:
        print("you have chosen a", weapon_choice)
    focus_choice = input("which focus do you want: ").lower()
    if focus_choice == "component pouch":
        print("you have chosen a component pouch")
    elif focus_choice == "arcane focus":
        print("you have chosen an arcane focus")
    else:
        print("you have chosen a", focus_choice)
    pack_choice = input("which pack do you want: ").lower()
    if pack_choice == "scholar's pack":
        print("you have chosen a scholar's pack")
    elif pack_choice == "explorer's pack":
        print("you have chosen an explorer's pack")
    else:
        print("you have chosen a", pack_choice)
    print("you also get a spellbook")

#------------------------------------------------------------------------------------

elif class_choice == "skip":
    print("you have chosen to skip equipment selection")

else:
    print("equipment for this class is not yet implemented")

print("-----End of Equipment Selection-----")

print("time to choose your background")
background_list = ["acolyte", "criminal", "folk hero", "noble", "sage", "soldier", "urchin", "skip"]
print("choose a background")
for background in background_list:
    print(background.capitalize())
print("--------------------------------")
selected = False
while selected == False:
    background_choice = input("What background would you like to play: ").lower().strip()
    if background_choice in background_list:
        print("You have chosen", background_choice.capitalize())
        selected = True
    else:
        print("You have to choose a valid background.")
if background_choice == "skip":
    print("you have chosen to skip background selection")
else:
    print("you have chosen the", background_choice, "background")
print("-----End of Background Selection-----")

print("time to choose your name")
name = input("what is your character's name: ").strip().capitalize()    
print("your character's name is", name)

#---------------------------------------

print("---------------------------------------")

print("time to choose your alignment")
alignment_list = ["lawful good", "neutral good", "chaotic good", "lawful neutral", "true neutral", "chaotic neutral", "lawful evil", "neutral evil", "chaotic evil"]
print("choose an alignment")
for alignment in alignment_list:
    print(alignment.capitalize())
print("--------------------------------")
selected = False
while selected == False:
    alignment_choice = input("What alignment would you like to play: ").lower().strip()
    if alignment_choice in alignment_list:
        print("You have chosen", alignment_choice.capitalize())
        selected = True
    else:
        print("You have to choose a valid alignment.")
print("your character's alignment is", alignment_choice)

print("---------------------------------------")

print("time to choose your age")
age = input("what is your character's age: ").strip()    
print("your character's age is", age)   
print("---------------------------------------")

#-----------[spell selection]-----------------

print("time to choose your spells")
if class_choice in ["bard", "cleric", "druid", "sorcerer", "warlock", "wizard"]:
    print("you can choose 3 level 1 spells to start with")
    spell_list = ["acid splash", "blade ward", "chill touch", "dancing lights", "fire bolt", "friends", "light", "mage hand", "mending", "message", "minor illusion", "poison spray", "prestidigitation", "ray of frost", "shocking grasp", "true strike"]
    for spell in spell_list:
        print(spell.capitalize())
    selected_spells = []
    while len(selected_spells) < 3:
        spell_choice = input("choose a spell: ").lower().strip()
        if spell_choice in spell_list and spell_choice not in selected_spells:
            selected_spells.append(spell_choice)
            print("you have chosen", spell_choice)
        elif spell_choice in selected_spells:
            print("you have already chosen that spell")
        else:
            print("that is not a valid spell")
    print("you have chosen the following spells:")
    for spell in selected_spells:
        print(spell.capitalize())
else:
    print("your class does not have any spells to choose from")
print("-----End of Spells Selection-----")

# inspiration from: https://github.com/github-copilot/code_referencing?cursor=252a579ed86acb3fd19a9b01d81952a2,c709745cbb3bc0158fb58ed949a3ef9a,f8ae8058cb63257292a9437379552279

print("---------------------------------------")
print("")

print("time to choose your character's appearance")
hair_color = input("what is your character's hair color: ").strip().capitalize()    
eye_color = input("what is your character's eye color: ").strip().capitalize()  
height = input("what is your character's height: ").strip().capitalize()  
weight = input("what is your character's weight: ").strip().capitalize()
sex = input("what is your character's sex: ").strip().capitalize()
print("your character's appearance is as follows:")

print("---------------------------------------")

print("hair color:", hair_color)

print("---------------------------------------")

print("eye color:", eye_color)  

print("---------------------------------------")

print("height:", height)

print("---------------------------------------")

print("weight:", weight)

print("---------------------------------------")

print("-----------[skill selection]-----------------")

print("time to choose your skills")
if class_choice == "barbarian":
    print("you can choose two skills from the following list:")
    skill_list = ["animal handling", "athletics", "intimidation", "nature", "perception", "survival"]
    for skill in skill_list:
        print(skill.capitalize())
    selected_skills = []
    while len(selected_skills) < 2:
        skill_choice = input("choose a skill: ").lower().strip()
        if skill_choice in skill_list and skill_choice not in selected_skills:
            selected_skills.append(skill_choice)
            print("you have chosen", skill_choice)
        elif skill_choice in selected_skills:
            print("you have already chosen that skill")
        else:
            print("that is not a valid skill")
    print("you have chosen the following skills:")
    for skill in selected_skills:
        print(skill.capitalize())

#------------------------------------------------------------------------------------        

elif class_choice == "bard":
    print("you can choose three skills from the following list:")
    skill_list = ["acrobatics", "animal handling", "arcana", "athletics", "deception", "history", "insight", "intimidation", "investigation", "medicine", "nature", "perception", "performance", "persuasion", "religion", "sleight of hand", "stealth", "survival"]
    for skill in skill_list:
        print(skill.capitalize())
    selected_skills = []
    while len(selected_skills) < 3:
        skill_choice = input("choose a skill: ").lower().strip()
        if skill_choice in skill_list and skill_choice not in selected_skills:
            selected_skills.append(skill_choice)
            print("you have chosen", skill_choice)
        elif skill_choice in selected_skills:
            print("you have already chosen that skill")
        else:
            print("that is not a valid skill")
    print("you have chosen the following skills:")
    for skill in selected_skills:
        print(skill.capitalize())

#------------------------------------------------------------------------------------        

elif class_choice == "cleric":
    print("you can choose two skills from the following list:")
    skill_list = ["history", "insight", "medicine", "persuasion", "religion"]
    for skill in skill_list:
        print(skill.capitalize())
    selected_skills = []
    while len(selected_skills) < 2:
        skill_choice = input("choose a skill: ").lower().strip()
        if skill_choice in skill_list and skill_choice not in selected_skills:
            selected_skills.append(skill_choice)
            print("you have chosen", skill_choice)
        elif skill_choice in selected_skills:
            print("you have already chosen that skill")
        else:
            print("that is not a valid skill")
    print("you have chosen the following skills:")
    for skill in selected_skills:
        print(skill.capitalize())

#------------------------------------------------------------------------------------

elif class_choice == "druid":
    print("you can choose two skills from the following list:")
    skill_list = ["arcana", "animal handling", "insight", "medicine", "nature", "perception", "religion", "survival"]
    for skill in skill_list:
        print(skill.capitalize())
    selected_skills = []
    while len(selected_skills) < 2:
        skill_choice = input("choose a skill: ").lower().strip()
        if skill_choice in skill_list and skill_choice not in selected_skills:
            selected_skills.append(skill_choice)
            print("you have chosen", skill_choice)
        elif skill_choice in selected_skills:
            print("you have already chosen that skill")
        else:
            print("that is not a valid skill")
    print("you have chosen the following skills:")
    for skill in selected_skills:
        print(skill.capitalize())

#------------------------------------------------------------------------------------

elif class_choice == "fighter":
    print("you can choose two skills from the following list:")
    skill_list = ["acrobatics", "animal handling", "athletics", "history", "insight", "intimidation", "perception", "survival"]
    for skill in skill_list:
        print(skill.capitalize())
    selected_skills = []
    while len(selected_skills) < 2:
        skill_choice = input("choose a skill: ").lower().strip()
        if skill_choice in skill_list and skill_choice not in selected_skills:
            selected_skills.append(skill_choice)
            print("you have chosen", skill_choice)
        elif skill_choice in selected_skills:
            print("you have already chosen that skill")
        else:
            print("that is not a valid skill")
    print("you have chosen the following skills:")
    for skill in selected_skills:
        print(skill.capitalize())

#------------------------------------------------------------------------------------

elif class_choice == "monk":
    print("you can choose two skills from the following list:")
    skill_list = ["acrobatics", "athletics", "history", "insight", "religion", "stealth"]
    for skill in skill_list:
        print(skill.capitalize())
    selected_skills = []
    while len(selected_skills) < 2:
        skill_choice = input("choose a skill: ").lower().strip()
        if skill_choice in skill_list and skill_choice not in selected_skills:
            selected_skills.append(skill_choice)
            print("you have chosen", skill_choice)
        elif skill_choice in selected_skills:
            print("you have already chosen that skill")
        else:
            print("that is not a valid skill")
    print("you have chosen the following skills:")
    for skill in selected_skills:
        print(skill.capitalize())

#------------------------------------------------------------------------------------

elif class_choice == "paladin":
    print("you can choose two skills from the following list:")
    skill_list = ["athletics", "insight", "intimidation", "medicine", "persuasion", "religion"]
    for skill in skill_list:
        print(skill.capitalize())
    selected_skills = []
    while len(selected_skills) < 2:
        skill_choice = input("choose a skill: ").lower().strip()
        if skill_choice in skill_list and skill_choice not in selected_skills:
            selected_skills.append(skill_choice)
            print("you have chosen", skill_choice)
        elif skill_choice in selected_skills:
            print("you have already chosen that skill")
        else:
            print("that is not a valid skill")
    print("you have chosen the following skills:")
    for skill in selected_skills:
        print(skill.capitalize())

#------------------------------------------------------------------------------------

elif class_choice == "ranger":
    print("you can choose three skills from the following list:")
    skill_list = ["animal handling", "athletics", "insight", "investigation", "nature", "perception", "stealth", "survival"]
    for skill in skill_list:
        print(skill.capitalize())
    selected_skills = []
    while len(selected_skills) < 3:
        skill_choice = input("choose a skill: ").lower().strip()
        if skill_choice in skill_list and skill_choice not in selected_skills:
            selected_skills.append(skill_choice)
            print("you have chosen", skill_choice)
        elif skill_choice in selected_skills:
            print("you have already chosen that skill")
        else:
            print("that is not a valid skill")
    print("you have chosen the following skills:")
    for skill in selected_skills:
        print(skill.capitalize())

#------------------------------------------------------------------------------------

elif class_choice == "rogue":
    print("you can choose four skills from the following list:")
    skill_list = ["acrobatics", "athletics", "deception", "insight", "intimidation", "investigation", "perception", "performance", "persuasion", "sleight of hand", "stealth"]
    for skill in skill_list:
        print(skill.capitalize())
    selected_skills = []
    while len(selected_skills) < 4:
        skill_choice = input("choose a skill: ").lower().strip()
        if skill_choice in skill_list and skill_choice not in selected_skills:
            selected_skills.append(skill_choice)
            print("you have chosen", skill_choice)
        elif skill_choice in selected_skills:
            print("you have already chosen that skill")
        else:
            print("that is not a valid skill")
    print("you have chosen the following skills:")
    for skill in selected_skills:
        print(skill.capitalize())

#------------------------------------------------------------------------------------

elif class_choice == "sorcerer":
    print("you can choose two skills from the following list:")
    skill_list = ["arcana", "deception", "insight", "intimidation", "persuasion", "religion"]
    for skill in skill_list:
        print(skill.capitalize())
    selected_skills = []
    while len(selected_skills) < 2:
        skill_choice = input("choose a skill: ").lower().strip()
        if skill_choice in skill_list and skill_choice not in selected_skills:
            selected_skills.append(skill_choice)
            print("you have chosen", skill_choice)
        elif skill_choice in selected_skills:
            print("you have already chosen that skill")
        else:
            print("that is not a valid skill")
    print("you have chosen the following skills:")
    for skill in selected_skills:
        print(skill.capitalize())

#------------------------------------------------------------------------------------

elif class_choice == "warlock":
    print("you can choose two skills from the following list:")
    skill_list = ["arcana", "deception", "history", "intimidation", "investigation", "nature", "religion"]
    for skill in skill_list:
        print(skill.capitalize())
    selected_skills = []
    while len(selected_skills) < 2:
        skill_choice = input("choose a skill: ").lower().strip()
        if skill_choice in skill_list and skill_choice not in selected_skills:
            selected_skills.append(skill_choice)
            print("you have chosen", skill_choice)
        elif skill_choice in selected_skills:
            print("you have already chosen that skill")
        else:
            print("that is not a valid skill")
    print("you have chosen the following skills:")
    for skill in selected_skills:
        print(skill.capitalize())

#------------------------------------------------------------------------------------

elif class_choice == "wizard":
    print("you can choose two skills from the following list:")
    skill_list = ["arcana", "history", "insight", "investigation", "medicine", "religion"]
    for skill in skill_list:
        print(skill.capitalize())
    selected_skills = []
    while len(selected_skills) < 2:
        skill_choice = input("choose a skill: ").lower().strip()
        if skill_choice in skill_list and skill_choice not in selected_skills:
            selected_skills.append(skill_choice)
            print("you have chosen", skill_choice)
        elif skill_choice in selected_skills:
            print("you have already chosen that skill")
        else:
            print("that is not a valid skill")
    print("you have chosen the following skills:")
    for skill in selected_skills:
        print(skill.capitalize())

#------------------------------------------------------------------------------------

elif class_choice == "skip":
    print("you have chosen to skip skill selection")

else:
    print("skill selection for this class is not yet implemented")

print("-----End of Skill Selection-----")

#------------------------------------------------------------------------------------


#-----------------------[summary]--------------------------

print("character creation complete!")
print("-----Final Caracther Summary-----")
print( )

print(f"race: {race_choice}")

print(f"alignment: {alignment_choice}")

print(f"background: {background_choice}")

print(f"hit points: {hit_points}")
try: 
    print(f"spells: {selected_spells}")

except:
    print("spells: none")

#-------------------------------------
thisdict = {
  "name": name,
  "age": age,
  "weight": weight,
  "eye color": eye_color,
  "hair color": hair_color,
  "class": class_choice
}

#-------------------------------------

thisdict["weapon"] = weapon_choice
thisdict["armor"] = armor_choice
thisdict["ranged weapon"] = ranged_weapon_choice
thisdict["pack"] = pack_choice
thisdict["focus"] = focus_choice
# -------------------------------------
# not sure if this is needed?

#--------------------------------------

thisdict = {
    "armor": armor_choice,
    "weapon": weapon_choice,
    "ranged weapon": ranged_weapon_choice,
    "pack": pack_choice,
    "focus": focus_choice
}


#-------------------------------------

thisdict = {
    "strength": stats["strength"],
    "dexterity": stats["dexterity"],
    "constitution": stats["constitution"],
    "intelligence": stats["intelligence"],
    "wisdom": stats["wisdom"],
    "charisma": stats["charisma"]
}

#-------------------------------------
# printing the dictionary in a more readable way

for x in thisdict:
  if thisdict[x]:
    print(f"{x} is {thisdict[x]}".capitalize()) 


print( )


print("-----End of Summary-----")

print("good luck on your adventures!")

#------------------------------------------------------------------------------------
# inspiration from:DnD Beyond, Roll20, GitHub Copilot, ChatGPT, Stack Overflow, and vai-tv
# thanks vai-tv <3 for helping me with making the code better!
# thanks to GitHub Copilot for helping me with some parts of the code!
# thanks to DnD Beyond and Roll20 for helping me with the rules and stuff!
# made by theluxmaster06
#---------------------------------------------