money = int(input("Enter the amount of money you have: "))
while True:

 if money <= 0:
    print("Invalid amount. Money cannot be zero or negative.")  
    exit()                                           


 elif money > 1000000000: 
    print("You have too much money to gamble. The maximum allowed is 1,000,000,000.")
    exit()  
 elif money < 10:
    print("You need at least 10 to gamble.")
    exit()
 elif money >= 10:
    print("You have", money, "to gamble with.")
    bet = int(input("Enter the amount you want to bet (minimum 10): "))
    if bet < 10:
        print("You need to bet at least 10.")
        exit()
    elif bet > money:
        print("You cannot bet more than you have.")
        exit()
    else:
        import random
        outcome = random.choice(["win", "lose"])
        if outcome == "win":
            money += bet
            print("You won! You now have", money)
        else:
            money -= bet
            print("You lost! You now have", money)  
        if money == 0:
            print("You have no money left to gamble.")
            print("want to sell ur house?")
            sell = input("yes or no: ").lower()
            if sell == "yes":
                print("you sold your house and got 1,000,000")
                money += 1000000
                print("you now have", money)
