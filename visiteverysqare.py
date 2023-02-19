import random

class MonopolyBoard:
    def __init__(self):
        self.squares = list(range(40))
        self.position = 0
        self.roll_count = 0
        self.circuit_count = 0
        self.visited = [False] * 40

    def roll_dice(self):
        return random.randint(1, 6), random.randint(1, 6)

    def move(self, steps):
        self.position = (self.position + steps) % 40
        self.visited[self.position] = True

    def play(self):
        while not all(self.visited):
            self.roll_count += 1
            dice1, dice2 = self.roll_dice()
            self.move(dice1 + dice2)
            if self.position == 0:
                self.circuit_count += 1
            elif self.position == 30:
                self.position = 10
        return self.roll_count, self.circuit_count

# Simulate the game 100,000 times and calculate the average number of rolls and circuits completed
total_rolls = 0
total_circuits = 0
games_played = 100000

for i in range(games_played):
    board = MonopolyBoard()
    rolls, circuits = board.play()
    total_rolls += rolls
    total_circuits += circuits

average_rolls = total_rolls / games_played
average_circuits = total_circuits / games_played

print("Average number of rolls:", average_rolls)
print("Average number of circuits completed:", average_circuits)
