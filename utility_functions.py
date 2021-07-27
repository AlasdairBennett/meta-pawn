import numpy as np
import pandas as pd


# get_games takes the name of a file containing chess game data and returns a dataframe containing
#   only the data of ranked games in that file
def get_games(filename='project/static/games.csv'):
    games = pd.read_csv(filename)

    # prune the unranked games from the data set
    ranked_games = games[games['rated']]

    return ranked_games


# global utility variable to avoid calling get_games repeatedly
chess_games_utility = get_games()


# get_rel_game_set takes in a set of chess games and an elo
# and returns the relevant data set that the suggestion should be based on
# in the future this function can include more features such as the increment code
# to be more granular with a bigger data set
def get_rel_game_set(game_set, user_rating):
    rel_game_set = game_set[(np.abs(game_set['white_rating'] - user_rating) < 100)
                            & (np.abs(game_set['black_rating'] - user_rating) < 100)]

    opening_outliers = get_opening_outliers(rel_game_set)
    return rel_game_set[~rel_game_set['opening_name'].isin(opening_outliers)]


# get_win_rate takes a opening name and set of chess games
# then returns the opening name, white/black win rate and number of games played for that opening in a tuple
def get_win_rate(games_set, opening_name):
    games_with_opening = games_set[games_set['opening_name'] == opening_name]

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
    games_set_t = games_set_t[~(games_set_t['winner'] == 'draw')]
    win_rates_table = pd.DataFrame([get_win_rate(games_set_t, x) for x in games_set_t['opening_name'].drop_duplicates()],
                                   columns=('opening_name', 'w_win_rate', 'b_win_rate', 'n_games_played'))

    return win_rates_table


# take in a set of chess game
# and return the average rating of the players that play each opening
def get_avg_elo(games_set):
    games_set_t = games_set.copy()
    games_set_t = games_set_t[~(games_set_t['winner'] == 'draw')]
    means_by_opening = games_set_t.groupby("opening_name").mean()
    means_by_opening.reset_index(inplace=True)
    means_by_opening = means_by_opening.rename(columns={'white_rating': 'avg_white_rating',
                                                        'black_rating': 'avg_black_rating'})
    return means_by_opening[['opening_name', 'avg_white_rating', 'avg_black_rating']].copy()


# White #


# Get beginner white games
def get_beginner_white_games(games_set):
    white_games = games_set[games_set['winner'] == 'white']
    beginner_white_games = white_games[white_games['white_rating'] <= 1500]
    beginner_white_games = beginner_white_games.assign(
        score_delta=beginner_white_games.white_rating - beginner_white_games.black_rating)
    return beginner_white_games


# Get intermediate white games
def get_intermediate_white_games(games_set):
    white_games = games_set[games_set['winner'] == 'white']
    intermediate_white_games = white_games[(white_games['white_rating'] > 1500) &
                                           (white_games['white_rating'] <= 2000)]
    intermediate_white_games = intermediate_white_games.assign(
        score_delta=intermediate_white_games.white_rating - intermediate_white_games.black_rating)
    return intermediate_white_games


# Get advanced white games
def get_advanced_white_games(games_set):
    white_games = games_set[games_set['winner'] == 'white']
    advanced_white_games = white_games[white_games['white_rating'] > 2000]
    advanced_white_games = advanced_white_games.assign(
        score_delta=advanced_white_games.white_rating - advanced_white_games.black_rating)
    return advanced_white_games


# Black #


# Get beginner black games
def get_beginner_black_games(games_set):
    black_games = games_set[games_set['winner'] == 'black']
    beginner_black_games = black_games[black_games['black_rating'] <= 1500]
    beginner_black_games = beginner_black_games.assign(
        score_delta=beginner_black_games.black_rating - beginner_black_games.white_rating)
    return beginner_black_games


# Get intermediate black games
def get_intermediate_black_games(games_set):
    black_games = games_set[games_set['winner'] == 'black']
    intermediate_black_games = black_games[(black_games['black_rating'] > 1500) &
                                           (black_games['black_rating'] <= 2000)]
    intermediate_black_games = intermediate_black_games.assign(
        score_delta=intermediate_black_games.black_rating - intermediate_black_games.white_rating)
    return intermediate_black_games


# Get advanced black games
def get_advanced_black_games(games_set):
    black_games = games_set[games_set['winner'] == 'black']
    advanced_black_games = black_games[black_games['black_rating'] > 2000]
    advanced_black_games = advanced_black_games.assign(
        score_delta=advanced_black_games.black_rating - advanced_black_games.white_rating)
    return advanced_black_games


# Utility methods #


# Get average score delta for each opening
def get_avg_delta(games_set):
    games_set_ = games_set.copy()

    black_games = games_set_[games_set_['winner'] == 'black']
    black_games = black_games.assign(rating_delta=black_games.black_rating - black_games.white_rating)

    white_games = games_set_[games_set_['winner'] == 'white']
    white_games = white_games.assign(rating_delta=white_games.white_rating - white_games.black_rating)

    games_set_ = pd.concat([white_games, black_games])

    means_by_opening = games_set_.groupby("opening_name").mean()
    means_by_opening.reset_index(inplace=True)
    means_by_opening = means_by_opening.rename(columns={'rating_delta': 'avg_rating_delta'})
    return means_by_opening[['opening_name', 'avg_rating_delta']].copy()


# remove the openings that are considered outliers using
# the instructions from this link https://www.wikihow.com/Calculate-Outliers
def get_opening_outliers(games_set):
    opening_freq = games_set['opening_name'].value_counts()
    l_quantile = opening_freq.quantile(0.25)
    h_quantile = opening_freq.quantile(0.75)
    interquartile_r = h_quantile - l_quantile

    return opening_freq[(opening_freq.values < l_quantile - 1.5 * interquartile_r)
                        | (opening_freq.values > h_quantile + 1.5 * interquartile_r)].index
