import pickle

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from kneed import KneeLocator

if __name__ == '__main__':
    print("running...")
    pd.set_option('display.max_columns', 20)
    pd.set_option('display.max_rows', 20)
    pd.set_option('display.width', 10000)
    openings = pd.read_csv('project/static/openings.csv')
    openings_features = openings.drop('opening_name', axis=1)
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(openings_features)

    kmeans_kwargs = {
        "init": "random",
        "n_init": 10,
        "max_iter": 300,
        "random_state": 88,
    }
    sse = []
    for k in range(1, 21):
        kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
        kmeans.fit(scaled_features)
        sse.append(kmeans.inertia_)

    plt.plot(range(1, 21), sse)
    plt.xticks(range(1, 21))
    plt.xlabel("Number of Clusters")
    plt.ylabel("SSE")
    plt.show()
    kl = KneeLocator(range(1, 21), sse, curve="convex", direction="decreasing")
    n = kl.elbow
    kmeans = KMeans(n_clusters=n)
    kmeans.fit(scaled_features)
    pickle.dump(kmeans, open("project/static/model/kmeans_model.pkl", "wb"))

