import pandas as pd
import matplotlib.pyplot as plt
import pickle
import numpy as np

if __name__ == '__main__':
    print("running...")
    pd.set_option('display.max_columns', 20)
    pd.set_option('display.max_rows', 20)
    pd.set_option('display.width', 10000)
    kmeans = pickle.load(open("project/static/model/kmeans_model.pkl", "rb"))
    openings = pd.read_csv('project/static/openings.csv')
    openings = openings.assign(cluster=kmeans.labels_)

    print(openings)
    u_labels = np.unique(kmeans.labels_)

    for i in u_labels:
        plt.scatter(openings[openings['cluster'] == i, openings['avg_rating_delta']],
                    openings[openings['cluster'] == i, openings['n_games_played']])
    plt.legend()
    plt.show()
