import json
from time import time

print("time to play your character!")

#--------------------------------------
print("now u have to choose wich caracther u want to play")
print("u can choose to play as the caracther u just created, or u can choose to play as a random caracther")
print("if u want to play as the caracther u just created, type 'created'")
print("if u want to play as a random caracther, type 'random'")
play_choice = input("type here: ").lower().strip()

if play_choice == "created":
    try:
        with open("character.json", "r") as f:
            character = json.load(f)
        print("Character loaded successfully!")
        print(json.dumps(character, indent=4))
    except Exception as e:
        print("Failed to load character:", e)

elif play_choice == "random":
    try:
        with open("characters.json", "r") as f:
            characters = json.load(f)
        import random
        character = random.choice(characters)
        print("Random character selected successfully!")
        print(json.dumps(character, indent=4))
    except Exception as e:
        print("Failed to load characters:", e)

else:
    print("Invalid choice. Please restart the program and choose either 'created' or 'random'.")

#--------------------------------------

print("time to play as the character u chose!")
start_time = time()
 

while True:
    print("\n--- Game Loop ---")
    elapsed_time = time() - start_time
    print(f"Elapsed Time: {elapsed_time:.2f} seconds")

    print("here is what u can do:")
    print("1. Attack")
    print("2. Defend")
    print("3. Explore")
    print("4. Rest")

    action = input("What do you want to do? (type 'exit' to quit): ").strip().lower()
    if action == "exit":
        print("Exiting the game. Goodbye!")
        break
    else:
        print(f"You chose to: {action}")

        if action not in ["attack", "defend", "explore", "rest"]:
            print("Invalid action. Please choose a valid option.")
            continue
        else:
            print(f"Action '{action}' executed successfully!")
    continue
#-------------------------------------- 
       