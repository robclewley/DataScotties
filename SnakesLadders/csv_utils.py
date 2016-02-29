"""
Utilities for working with CSV files representing all game move data.

EXAMPLE USAGE:

all_data = multi_run(n)
save_csv(all_data, filename)

all_data = load_csv(filename)

...  for a given number of runs, n, and a string filename parameter.
"""
import pandas as pd

def save_csv(all_data, filename):
    """Save list of game move DataFrames to the given filename.
    """
    # Add game number column to each df to allow for stacking
    all_data_mod = []
    for i, df in enumerate(all_data):
        df.insert(0, 'n', i)
        all_data_mod.append(df)
    all_data_df = pd.concat(all_data_mod)
    all_data_df.to_csv(filename, header=True)

def load_csv(filename):
    """
    Return list of game move DataFrames loaded from given filename.
    """
    all_data_df = pd.read_csv(filename)
    all_data = []
    for name, group in all_data_df.groupby(['n']):
        # strip game number column, reset index to 0
        df = group[['die','kind', 'start', 'end']].reset_index(drop=True)
        all_data.append(df)
    return all_data

def convert_records(records):
    """
    records is a list of dicts
    """
    d = {'die': [],
        'start': [],
        'end': [],
        'kind': []
        }
    for recdict in records:
        for k in ('die', 'start', 'end', 'kind'):
            d[k].append(recdict[k])
    return pd.DataFrame(d)

def multi_run(game, n):
    """game parameter is a GameFSM object, n is number of times to run game.
    Returns list of dataframes created from move records (using convert_records)
    """
    all_data = []
    for i in range(n):
        game.run()
        all_data.append(convert_records(game.records))
    return all_data