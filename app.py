from project import create_app
import pandas as pd

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


# get_opening_frequency takes a dataframe containing chess match information and returns a dataframe
#   containing the most common chess openings in the match information dataframe
def get_opening_frequency(games):
    return games['opening_name'].value_counts()


def get_win_rate(opening_name, elo_low = -1, elo_high = -1):
    chess_games = get_games('project/static/games.csv')
    games = chess_games[chess_games['opening_name'] == opening_name]
    w_win = games[games['winner'] == 'white']
    b_win = games[games['winner'] == 'black']

    w_win_rate = len(w_win) * 100 / len(games)
    b_win_rate = len(b_win) * 100 / len(games)

    return w_win_rate, b_win_rate


if __name__ == "__main__":
    print("running...")

    pd.set_option('display.max_columns', 20)
    pd.set_option('display.max_rows', 20)
    pd.set_option('display.width', 10000)

    chess_games = get_games('project/static/games.csv')
    print(chess_games.iloc[:10])
    opening_freq = get_opening_frequency(chess_games)
    print(opening_freq[:10])
    rating = 1000
    black_lose_opening_freq = get_opening_frequency(
        chess_games[(chess_games.black_rating < rating) & (chess_games.winner == 'white')])

    print(get_win_rate('King\'s Pawn Game: Leonardis Variation'))
