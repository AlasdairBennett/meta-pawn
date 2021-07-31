import pickle
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if __name__ == '__main__':
    print("running...")
    pd.set_option('display.max_columns', 20)
    pd.set_option('display.max_rows', 20)
    pd.set_option('display.width', 10000)

    w_openings = pd.read_csv('project/static/w_clusters.csv')

    u_labels = np.unique(w_openings['cluster'])
    for i in u_labels:
        plt.scatter(w_openings[w_openings['cluster'] == i]['avg_rating_delta'],
                    w_openings[w_openings['cluster'] == i]['w_win_rate'], label=i)
    plt.xlabel('avg_rating_delta')
    plt.ylabel('w_win_rate')
    plt.legend()
    plt.show()

    for i in u_labels:
        plt.scatter(w_openings[w_openings['cluster'] == i]['w_win_rate'],
                    w_openings[w_openings['cluster'] == i]['n_games_played'], label=i)
    plt.xlabel('w_win_rate')
    plt.ylabel('n_games_played')
    plt.legend()
    plt.show()

    for i in u_labels:
        plt.scatter(w_openings[w_openings['cluster'] == i]['avg_white_rating'],
                    w_openings[w_openings['cluster'] == i]['w_win_rate'], label=i)
    plt.xlabel('avg_white_rating')
    plt.ylabel('w_win_rate')
    plt.legend()
    plt.show()

    for i in u_labels:
        plt.scatter(w_openings[w_openings['cluster'] == i]['avg_white_rating'],
                    w_openings[w_openings['cluster'] == i]['n_games_played'], label=i)
    plt.xlabel('avg_white_rating')
    plt.ylabel('n_games_played')
    plt.legend()
    plt.show()

    b_openings = pd.read_csv('project/static/b_clusters.csv')

    u_labels = np.unique(b_openings['cluster'])
    for i in u_labels:
        plt.scatter(b_openings[b_openings['cluster'] == i]['avg_rating_delta'],
                    b_openings[b_openings['cluster'] == i]['b_win_rate'], label=i)
    plt.xlabel('avg_rating_delta')
    plt.ylabel('b_win_rate')
    plt.legend()
    plt.show()

    for i in u_labels:
        plt.scatter(b_openings[b_openings['cluster'] == i]['b_win_rate'],
                    b_openings[b_openings['cluster'] == i]['n_games_played'], label=i)
    plt.xlabel('b_win_rate')
    plt.ylabel('n_games_played')
    plt.legend()
    plt.show()

    for i in u_labels:
        plt.scatter(b_openings[b_openings['cluster'] == i]['avg_black_rating'],
                    b_openings[b_openings['cluster'] == i]['b_win_rate'], label=i)
    plt.xlabel('avg_black_rating')
    plt.ylabel('b_win_rate')
    plt.legend()
    plt.show()

    for i in u_labels:
        plt.scatter(b_openings[b_openings['cluster'] == i]['avg_black_rating'],
                    b_openings[b_openings['cluster'] == i]['n_games_played'], label=i)
    plt.xlabel('avg_black_rating')
    plt.ylabel('n_games_played')
    plt.legend()
    plt.show()
