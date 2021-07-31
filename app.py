import pandas as pd

import utility_functions as uf
from project import create_app

app = create_app()

# Global variables to be piped through routes.py to be displayed on front end
chess_games = uf.get_games('project/static/games.csv')
win_table_1 = uf.get_win_rate_table(uf.get_rel_game_set(chess_games, 1000))

# Inclusive of ALL data
beginner_white_games = uf.get_beginner_white_games(chess_games)
beginner_black_games = uf.get_beginner_black_games(chess_games)

intermediate_white_games = uf.get_intermediate_white_games(chess_games)
intermediate_black_games = uf.get_intermediate_black_games(chess_games)

advanced_white_games = uf.get_advanced_white_games(chess_games)
advanced_black_games = uf.get_advanced_black_games(chess_games)

# TODO (re)move this code block - I'm not sure what's important here
if __name__ == "__main__":
    print("running...")
    pd.set_option('display.max_columns', 20)
    pd.set_option('display.max_rows', 20)
    pd.set_option('display.width', 10000)

    print("Beginner white games:")
    beginner_white_avg_delta = uf.get_avg_delta(beginner_white_games)
    print(beginner_white_games.sample(10))
    print(beginner_white_avg_delta.sample(10))

    uf.get_winning_countplot(beginner_white_games, "Beginner White Top 10 Openings", "project/static/img/beg_whit_cp.png")
    uf.get_winning_countplot(intermediate_white_games, "Intermediate White Top 10 Openings", "project/static/img/int_whit_cp.png")
    uf.get_winning_countplot(advanced_white_games, "Advanced White Top 10 Openings", "project/static/img/adv_whit_cp.png")
    
    uf.get_winning_countplot(beginner_black_games, "Beginner Black Top 10 Openings", "project/static/img/beg_blk_cp.png")
    uf.get_winning_countplot(intermediate_black_games, "Intermediate Black Top 10 Openings", "project/static/img/int_blk_cp.png")
    uf.get_winning_countplot(advanced_black_games, "Advanced Black Top 10 Openings", "project/static/img/adv_blk_cp.png")

    #uf.get_rating_scatterplot(chess_games, 1000, "white_rating")
