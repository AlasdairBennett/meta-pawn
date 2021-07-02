from project import create_app
import pandas as pd

app = create_app()


###
# # get_games takes the name of a file containing chess game data and returns a dataframe containing
# #   only the data of ranked games
# def get_games(filename):
#     games = pd.read_csv('project/static/games.csv')
#
#     # prune the unranked games from the data set
#     ranked_games = games[games['rated'] == True]
#
#     return ranked_games
#
#
# # get_opening_frequency takes a dataframe containing chess match information and returns a dataframe
# #   containing the most common chess openings in the match information dataframe
# def get_opening_frequency(games):
#     return games['opening_name'].value_counts()
#
#
# if __name__ == "__main__":
#     print("running...")
#
#     pd.set_option('display.max_columns', 20)
#     pd.set_option('display.max_rows', 20)
#     pd.set_option('display.width', 10000)
#
#     chess_games = get_games('project/static/games.csv')
#     print(chess_games.iloc[:10])
#     opening_freq = get_opening_frequency(chess_games)
#     print(opening_freq[:10])
#     rating = 1000
#     black_lose_opening_freq = get_opening_frequency(chess_games[(chess_games.black_rating < rating) & (chess_games.winner == 'white')])
#     print(black_lose_opening_freq[:10])
