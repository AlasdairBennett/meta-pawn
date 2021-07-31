import pandas as pd

import utility_functions as uf
from project import create_app

app = create_app()

# Global variables to be piped through routes.py to be displayed on front end
chess_games = uf.get_games('project/static/games.csv')
win_table_1 = uf.get_win_rate_table(uf.get_rel_game_set(chess_games, 1000))

# TODO (re)move this code block - I'm not sure what's important here
if __name__ == "__main__":
    print("running...")
    pd.set_option('display.max_columns', 20)
    pd.set_option('display.max_rows', 20)
    pd.set_option('display.width', 10000)

