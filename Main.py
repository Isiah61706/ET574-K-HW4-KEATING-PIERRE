#Name: Isiah Keating-Pierre
#QCC ID: 24603122

import random

class Die: 
    def __init__(self, sides=6):
        self.sides = sides 
    def roll(self):
        return random.randint(1, self.sides)


class DiceGame:
    def __init__(self):
        self.die1 = Die()
        self.die2 = Die()
        self.history = []
    def evaluate_roll(self, total):
        if total in [7, 11]:
            return "Win"
        elif total in [2,3,12]:
            return "Lose"
        else:
            return "Roll Again"
    
    def play_round(self):
        roll1 = self.die1.roll()
        roll2 = self.die2.roll()
        total = roll1 + roll2
        result = self.evaluate_roll(total)
        self.history.append((roll1, roll2, total, result))
        return roll1, roll2, total, result

def main():
    game = DiceGame()
    history = []
    
    print("Welcome to the Dice Game!")
    
    while True:
        print("\nMenu:")
        print("1. Play a round")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == '1':
            roll1, roll2, total, result = game.play_round()
            print(f"\nYou rolled {roll1} and {roll2}. Total = {total}")
            print(f"Result: {result}")
            history.append((roll1, roll2, total, result))
        
        elif choice == '2':
            print("\nThanks for playing! Here are your game results:\n")
            if len(history) == 0:
                print("No rounds played.")
        
            else:
                for i, (r1, r2, total, result) in enumerate(history, start=1):
                        print(f"Round {i}: {r1} + {r2} = {total} → {result}")
            print("\nGoodbye!")
            return
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()