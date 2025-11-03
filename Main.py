class die: 
    def __init__(self, sides=6):
        self.sides = sides 
    def roll(self)
        return random.randint(1,  self.sides)


class DiceGame:
    def __init__(self)
        self.die1 = die()
        self.die2 = die()
    def evaluate_roll(self, total):
        if total in [7, 11]:
            return "Win"
        elif total in [2,3,12]:
            return "Lose"
        else":
            return "Roll Again"
    
    def play_round(self)
    roll1 = self.die1.roll()
    roll2 = self.die2.roll()
    total = roll1 + roll2
    result = self.evaluate_roll(total)
    return roll1. roll2. total, result


