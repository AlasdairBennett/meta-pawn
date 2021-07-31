import pandas as pd
import matplotlib.pyplot as plt
import pickle
import numpy as np

if __name__ == '__main__':
    print("running...")
    pd.set_option('display.max_columns', 20)
    pd.set_option('display.max_rows', 20)
    pd.set_option('display.width', 10000)
    kmeans = pickle.load(open("project/static/models/w_model.pkl", "rb"))
    openings = pd.read_csv('project/static/openings.csv')

    openings = openings[(openings['w_win_rate'] >= openings['b_win_rate']) & (openings['n_games_played'] >= 10)]
    openings = openings.assign(cluster=kmeans.labels_)

    u_labels = np.unique(kmeans.labels_)
    for i in u_labels:
        plt.scatter(openings[openings['cluster'] == i]['avg_rating_delta'],
                    openings[openings['cluster'] == i]['w_win_rate'], label=i)
    plt.xlabel('avg_rating_delta')
    plt.ylabel('w_win_rate')
    plt.legend()
    plt.show()

    for i in u_labels:
        plt.scatter(openings[openings['cluster'] == i]['w_win_rate'],
                    openings[openings['cluster'] == i]['n_games_played'], label=i)
    plt.xlabel('w_win_rate')
    plt.ylabel('n_games_played')
    plt.legend()
    plt.show()

    for i in u_labels:
        plt.scatter(openings[openings['cluster'] == i]['avg_white_rating'],
                    openings[openings['cluster'] == i]['w_win_rate'], label=i)
    plt.xlabel('avg_white_rating')
    plt.ylabel('w_win_rate')
    plt.legend()
    plt.show()

    for i in u_labels:
        plt.scatter(openings[openings['cluster'] == i]['avg_white_rating'],
                    openings[openings['cluster'] == i]['n_games_played'], label=i)
    plt.xlabel('avg_white_rating')
    plt.ylabel('n_games_played')
    plt.legend()
    plt.show()
