import pandas as pd
import utility_functions as uf

# get_games returns a dataframe containing only the data of ranked games
if __name__ == "__main__":
    print("running...")
    pd.set_option('display.max_columns', 20)
    pd.set_option('display.max_rows', 20)
    pd.set_option('display.width', 10000)

    games = pd.read_csv('project/static/games.csv')

    # prune the unranked games from the data set
    ranked_games = games[games['rated']]
    avg_delta_table = uf.get_avg_delta(ranked_games)
    win_rate_table = uf.get_win_rate_table(ranked_games)

    opening_data = pd.merge(avg_delta_table, win_rate_table, on='opening_name')
    opening_data = opening_data.rename(columns={"rating_delta": "avg_rating_delta"})

    print(opening_data.sample(20))
    opening_data.to_csv('project/static/openings.csv')
