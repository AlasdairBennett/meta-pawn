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
    
    