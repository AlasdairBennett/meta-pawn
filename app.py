from project import create_app
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

app = create_app()


# def frame_html

##
# get_games takes the name of a file containing chess game data and returns a dataframe containing
#   only the data of ranked games
def get_games(filename):
    games = pd.read_csv('project/static/games.csv')

    # prune the unranked games from the data set
    ranked_games = games[games['rated'] == True]

    return ranked_games


chess_games = get_games('project/static/games.csv')


# get_opening_frequency takes a dataframe containing chess match information and returns a dataframe
#   containing the most common chess openings in the match information dataframe
def get_opening_frequency(games):
    return games['opening_name'].value_counts()


# get_win_rate takes a opening name and set of chess game
# then returns the opening name, white and black win rate for that opening in a tuple
def get_win_rate(games_set, opening_name):
    games_with_opening = games_set[chess_games['opening_name'] == opening_name]
    w_win = games_with_opening[games_with_opening['winner'] == 'white']
    b_win = games_with_opening[games_with_opening['winner'] == 'black']

    w_win_rate = len(w_win) * 100 / len(games_with_opening)
    b_win_rate = len(b_win) * 100 / len(games_with_opening)

    return opening_name, w_win_rate, b_win_rate


# get_win_rate_table takes set of chess game
# then returns table of white and black win rates for each opening in that set
def get_win_rate_table(games_set):
    games_set_t = games_set.copy()
    win_rates_table = pd.DataFrame([get_win_rate(games_set, x) for x in games_set_t['opening_name'].drop_duplicates()],
                                   columns=('opening_name', 'w_win_rate', 'b_win_rate'))

    return win_rates_table


if __name__ == "__main__":
    print("running...")

    pd.set_option('display.max_columns', 20)
    pd.set_option('display.max_rows', 20)
    pd.set_option('display.width', 10000)

    # chess_games = get_games('project/static/games.csv')
    print(chess_games.iloc[:10])
    opening_freq = get_opening_frequency(chess_games)
    print(opening_freq[:10])
    rating = 1000
    black_lose_opening_freq = get_opening_frequency(
        chess_games[(chess_games.black_rating < rating) & (chess_games.winner == 'white')])

    print(get_win_rate_table(chess_games))

    sns.pairplot(get_win_rate_table(chess_games))
    plt.show()
