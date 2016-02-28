import snakesladders as SL

def make_game_from_dict(setup):
    """
    `setup` parameter is a dictionary, e.g. loaded from JSON file
    Returns a GameFSM object configured from the dictionary.
    """
    game = SL.GameFSM(setup['size'])
    for s1, s2 in setup['snakes']:
        game.all_states[s1].link = s2
    for l1, l2 in setup['ladders']:
        game.all_states[l1].link = l2
    game.make_state_kinds()
    return game
