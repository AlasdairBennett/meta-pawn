import pandas as pd


# get_games takes the name of a file containing chess game data and returns a dataframe containing the same data
def get_games(filename):
    games = pd.read_csv('games.csv')

    return games


if __name__ == "__main__":
    print("running...")

    pd.set_option('display.max_columns', 20)
    pd.set_option('display.max_rows', 20)
    pd.set_option('display.width', 10000)

    games = get_games('games.csv')
    print(games.iloc[:10])
