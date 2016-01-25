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
        for ix in range(n+1):
            self.all_states.append(State(ix))

game = GameFSM(16)

print(game.all_states)

# Ladders

game.all_states[2].link = 10
game.all_states[8].link = 14

