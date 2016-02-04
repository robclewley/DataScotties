"""
Finite State Machine for Snakes and Ladders game

Kind character codes:
    S = Snake, L = Ladder (aka Chute), B = Blank

How to use:
1. Make a game object with the number of board squares
2. Create the links between state objects to define snakes or ladders
3. Call game.make_state_kinds() to finish initializations
4. Call game.run()
5. Access game.records object to see results
"""
# coding: utf-8

import random

class State(object):
    def __init__(self, ix):
        """index is the position on the board for this state instance.
        link is either None (normal blank location) or the index of a state connected
        by a snake or a ladder.
        """
        self.index = ix
        self.link = ix  # placeholder, not = index if Snake or Ladder
        self.kind = 'B'  # placeholder blank state (updated in first call to process)

    def make_kind(self):
        if self.link != self.index:
            if self.link > self.index:
                # ! this is inefficient because it gets re-updated every time
                # this method is called!
                self.kind = 'L'
            else:
                self.kind = 'S'
        else:
            # link is None: "Blank" = not a snake or ladder
            self.kind = 'B'

    def process(self):
        """Action when landed upon"""
        return self.link

    def __repr__(self):
        if self.kind == 'S':
            s = ', Snake'
        elif self.kind == 'L':
            s = ', Ladder'
        else:
            s = ''
        return "State({0}{1})".format(self.index, s)


class GameFSM(object):
    def __init__(self, n):
        # list of State objects for each position on the board
        self.all_states = []
        # current position of player on board
        #self.position = 0
        # size of board
        self.n = n
        # make empty board states for each position
        # (snake and ladder positions must be added later)
        for ix in range(n+1):
            blank_state = State(ix)
            self.all_states.append(blank_state)
        # record of moves, die rolls, and snake/ladder use
        #self.records = []
        # Reset method takes care of position and records
        self.reset()

    def make_state_kinds(self):
        """Must run this after creating the snakes and ladder links, before a game
        """
        for state in self.all_states:
            state.make_kind()

    def move_and_record(self, die):
        """die is an integer
        """
        start_pos = self.position
        inter_pos = self.position + die
        try:
            state_obj = self.all_states[inter_pos]
        except IndexError:
            # moved off the end of the board
            kind = 'B'
            final_pos = self.n
        else:
            final_pos = state_obj.process()
            kind = state_obj.kind
        self.position = final_pos
        # all this could be written more consisely as
        #self.position = self.all_states[self.position+die].process()
        record = {'start': start_pos,
                  'die': die,
                  'kind': kind,
                  'end': self.position}
        self.records.append(record)

    def reset(self):
        """Reset game state for a new game
        """
        self.position = 0
        self.records = []

    def run(self):
        """
        Run one whole game
        """
        self.reset()
        #print("Starting game!")
        while self.position < self.n:
            # roll die
            die = rollDie()
            #print("Die={}".format(die))
            # move based on die roll and record results
            self.move_and_record(die)
            #print("New position is {}".format(self.position))
        #print("Game over!")

# Find total number of moves from records
def count_moves(records):
    return len(records)

# Find number of snakes or ladders used in game
def count_snakes_and_ladders(records):
    """
    records is a list of dictionaries keyed with 'kind', 'start', 'end', 'die'
    Returns a pair (s, l) of counts of landing on any snake or ladder
    """
    tot_s = 0
    tot_l = 0
    for rec in records:
        if rec['kind'] == 'S':
            tot_s = tot_s + 1
        elif rec['kind'] == 'L':
            tot_l = tot_l + 1
    return tot_s, tot_l

def rollDie():
    return random.randint(1, DIE_SIDES)

# Global constant in caps
DIE_SIDES = 4
