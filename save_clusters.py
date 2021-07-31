import pickle
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

if __name__ == '__main__':
    print("running...")
    pd.set_option('display.max_columns', 20)
    pd.set_option('display.max_rows', 20)
    pd.set_option('display.width', 10000)
    openings = pd.read_csv('project/static/openings.csv')

    w_openings = openings[(openings['w_win_rate'] >= openings['b_win_rate']) & (openings['n_games_played'] >= 10)]
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(w_openings.drop(['opening_eco', 'opening_name'], axis=1))
    kmeans = pickle.load(open("project/static/models/w_model.pkl", "rb"))
    kmeans.fit(scaled_features)
    w_openings = w_openings.assign(cluster=kmeans.labels_)
    w_openings.to_csv('project/static/w_clusters.csv', index=False)

    b_openings = openings[(openings['w_win_rate'] <= openings['b_win_rate']) & (openings['n_games_played'] >= 10)]
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(b_openings.drop(['opening_eco', 'opening_name'], axis=1))
    kmeans = pickle.load(open("project/static/models/b_model.pkl", "rb"))
    kmeans.fit(scaled_features)
    b_openings = b_openings.assign(cluster=kmeans.labels_)
    b_openings.to_csv('project/static/b_clusters.csv', index=False)
