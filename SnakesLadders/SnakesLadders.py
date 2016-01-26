
# coding: utf-8

# ## Finite State Machine for Snakes and Ladders game

import random

class State(object):
    def __init__(self, ix):
        self.index = ix
        self.link = None  # placeholder, not None if Snake or Ladder

    def process(self):
        """Action when landed upon"""
        if self.link:
            if self.link > self.index:
                # Ladder!
                return self.link
            else:
                # Snake!
                return self.link
        else:
            # link is None: "Normal" = not a snake or ladder
            return self.index


class GameFSM(object):
    def __init__(self, n):
        self.all_states = []
        self.position = 0
        self.n = n
        for ix in range(n+1):
            self.all_states.append(State(ix))

    def move(self, die):
        """die is an integer
        """
        inter_pos = self.position + die
        state_obj = self.all_states[inter_pos]
        final_pos = state_obj.process()
        self.position = final_pos
        # all this could be written more consisely as
        #self.position = self.all_states[self.position+die].process()

    def run(self):
        print("Starting game!")
        while self.position < self.n:
            # roll die
            die = rollDie()
            # move based on die roll
            self.move(die)
            # record results
        print("Game over!")


# Global constant in caps
DIE_SIDES = 4

def rollDie():
    return random.randint(1, DIE_SIDES)

game = GameFSM(16)


# Ladders
game.all_states[2].link = 10
game.all_states[8].link = 14


# Snakes
game.all_states[11].link = 4
game.all_states[15].links = 6

print(game.all_states)

