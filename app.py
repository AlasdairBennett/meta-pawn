import numpy as np
from project import create_app
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

app = create_app()


# get_games takes the name of a file containing chess game data and returns a dataframe containing
#   only the data of ranked games
def get_games(filename):
    games = pd.read_csv('project/static/games.csv')

    # prune the unranked games from the data set
    ranked_games = games[games['rated']]

    return ranked_games


# get_rel_game_set takes in a set of chess games and an elo
# and returns the relevant data set that the suggestion should be based on
# in the future this function can include more features such as the increment code
# to be more granular with a bigger data set
def get_rel_game_set(game_set, user_rating):
    rel_game_set = game_set[(np.abs(game_set['white_rating'] - user_rating) < 100)
                            & (np.abs(game_set['black_rating'] - user_rating) < 100)]

    opening_outliers = get_opening_outliers(rel_game_set)
    return rel_game_set[rel_game_set['opening_name'].isin(opening_outliers)]


# get_win_rate takes a opening name and set of chess games
# then returns the opening name, white/black win rate and number of games played for that opening in a tuple
def get_win_rate(games_set, opening_name):
    games_with_opening = games_set[chess_games['opening_name'] == opening_name]
    w_win = games_with_opening[games_with_opening['winner'] == 'white']
    b_win = games_with_opening[games_with_opening['winner'] == 'black']

    n_games_played = len(games_with_opening)

    w_win_rate = len(w_win) * 100 / len(games_with_opening)
    b_win_rate = len(b_win) * 100 / len(games_with_opening)

    return opening_name, w_win_rate, b_win_rate, n_games_played


# get_win_rate_table takes set of chess game
# then returns table of white/black win rates and number of games played for each opening in that set
def get_win_rate_table(games_set):
    games_set_t = games_set.copy()
    win_rates_table = pd.DataFrame([get_win_rate(games_set, x) for x in games_set_t['opening_name'].drop_duplicates()],
                                   columns=('opening_name', 'w_win_rate', 'b_win_rate', 'n_games_played'))

    return win_rates_table


### White ###
# Get beginner white games
def get_beginner_white_games(games_set):
    white_games = games_set[games_set['winner'] == 'white']
    beginner_white_games = white_games[white_games['white_rating'] <= 1500]
    beginner_white_games = beginner_white_games.assign(score_delta = beginner_white_games.white_rating - beginner_white_games.black_rating)
    return beginner_white_games


# Get intermediate white games
def get_intermediate_white_games(games_set):
    white_games = games_set[games_set['winner'] == 'white']
    intermediate_white_games = white_games[(white_games['white_rating'] > 1500) &
                                           (white_games['white_rating'] <= 2000)]
    intermediate_white_games = intermediate_white_games.assign(score_delta = intermediate_white_games.white_rating - intermediate_white_games.black_rating)
    return intermediate_white_games  


# Get advanced white games
def get_advanced_white_games(games_set):
    white_games = games_set[games_set['winner'] == 'white']
    advanced_white_games = white_games[white_games['white_rating'] > 2000]
    advanced_white_games = advanced_white_games.assign(score_delta = advanced_white_games.white_rating - advanced_white_games.black_rating)
    return advanced_white_games


### Black ###
# Get beginner black games
def get_beginner_black_games(games_set):
    black_games = games_set[games_set['winner'] == 'black']
    beginner_black_games = black_games[black_games['black_rating'] <= 1500]
    beginner_black_games = beginner_black_games.assign(score_delta = beginner_black_games.black_rating - beginner_black_games.white_rating)
    return beginner_black_games


# Get intermediate black games
def get_intermediate_black_games(games_set):
    black_games = games_set[games_set['winner'] == 'black']
    intermediate_black_games = black_games[(black_games['black_rating'] > 1500) &
                                           (black_games['black_rating'] <= 2000)]
    intermediate_black_games = intermediate_black_games.assign(score_delta = intermediate_black_games.black_rating - intermediate_black_games.white_rating)
    return intermediate_black_games


# Get advanced black games
def get_advanced_black_games(games_set):
    black_games = games_set[games_set['winner'] == 'black']
    advanced_black_games = black_games[black_games['black_rating'] > 2000]
    advanced_black_games = advanced_black_games.assign(score_delta = advanced_black_games.black_rating - advanced_black_games.white_rating)
    return advanced_black_games


### Utility methods ###
# Get average score delta for each opening
def get_avg_delta(games_set):
    games_set = games_set[["opening_name", "score_delta"]]
    avg_delta = games_set.groupby("opening_name").mean()
    return avg_delta


# remove the openings that are considered outliers using
# the instructions from this link https://www.wikihow.com/Calculate-Outliers
def get_opening_outliers(games_set):
    opening_freq = games_set['opening_name'].value_counts()
    l_quantile = opening_freq.quantile(0.25)
    h_quantile = opening_freq.quantile(0.75)
    interquartile_r = h_quantile - l_quantile

    return opening_freq[(opening_freq.values < l_quantile - 1.5 * interquartile_r)
                        | (opening_freq.values > h_quantile + 1.5 * interquartile_r)].index


# Global variables to be piped through routes.py to be displayed on front end
chess_games = get_games('project/static/games.csv')
win_table_1 = get_win_rate_table(get_rel_game_set(chess_games, 1000))


if __name__ == "__main__":
    print("running...")
    pd.set_option('display.max_columns', 20)
    pd.set_option('display.max_rows', 20)
    pd.set_option('display.width', 10000)

    print(get_win_rate_table(chess_games))
    
    print("Beginner white games:")
    beginner_white_games = get_beginner_white_games(chess_games)
    beginner_avg_delta = get_avg_delta(beginner_white_games)
    print(beginner_white_games.sample(10))
    print(beginner_avg_delta)
    
    print("Beginner black games:")
    beginner_black_games = get_beginner_black_games(chess_games)
    #print(beginner_black_games.sample(10))
    
    print("Intermediate white games:")
    intermediate_white_games = get_intermediate_white_games(chess_games)
    #print(intermediate_white_games.sample(10))
    
    print("Intermediate black games:")
    intermediate_black_games = get_intermediate_black_games(chess_games)
    #print(intermediate_black_games.sample(10))
    
    print("Advanced white games:")
    advanced_white_games = get_advanced_white_games(chess_games)
    #print(advanced_white_games.sample(10))
    
    print("Advanced black games:")
    advanced_black_games = get_advanced_black_games(chess_games)
    #print(advanced_black_games.sample(10))
    
    sns.scatterplot(data=beginner_white_games, x="white_rating", y="opening_ply")
    plt.show()

    print(chess_games.columns)

    print(get_rel_game_set(chess_games, 1500).sample(20))

    sns.pairplot(get_win_rate_table(chess_games))
    plt.show()
