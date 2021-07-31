import pandas as pd

import utility_functions as uf

# this script generate a opening data set
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
    avg_rating_table = uf.get_avg_elo(ranked_games)

    opening_data = pd.merge(avg_delta_table, win_rate_table, on=['opening_eco', 'opening_name'])
    opening_data = pd.merge(opening_data, avg_rating_table, on=['opening_eco', 'opening_name'])
    opening_data.to_csv('project/static/openings.csv', index=False)
