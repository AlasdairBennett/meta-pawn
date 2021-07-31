### This is a script used to generate the plot figures ###
import utility_functions as uf

chess_games = uf.get_games('project/static/games.csv')

# Inclusive of ALL data
beginner_white_games = uf.get_beginner_white_games(chess_games)
beginner_black_games = uf.get_beginner_black_games(chess_games)

intermediate_white_games = uf.get_intermediate_white_games(chess_games)
intermediate_black_games = uf.get_intermediate_black_games(chess_games)

advanced_white_games = uf.get_advanced_white_games(chess_games)
advanced_black_games = uf.get_advanced_black_games(chess_games)

# Generate the plots
uf.get_winning_countplot(beginner_white_games, "Beginner White Top 10 Openings", "project/static/img/beg_whit_cp.png")
uf.get_winning_countplot(intermediate_white_games, "Intermediate White Top 10 Openings",
                         "project/static/img/int_whit_cp.png")
uf.get_winning_countplot(advanced_white_games, "Advanced White Top 10 Openings", "project/static/img/adv_whit_cp.png")

uf.get_winning_countplot(beginner_black_games, "Beginner Black Top 10 Openings", "project/static/img/beg_blk_cp.png")
uf.get_winning_countplot(intermediate_black_games, "Intermediate Black Top 10 Openings",
                         "project/static/img/int_blk_cp.png")
uf.get_winning_countplot(advanced_black_games, "Advanced Black Top 10 Openings", "project/static/img/adv_blk_cp.png")
