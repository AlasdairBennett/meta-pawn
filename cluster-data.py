import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

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
    for k in range(1, 20):
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(scaled_features)
        sse.append(kmeans.inertia_)

    plt.style.use("fivethirtyeight")
    plt.plot(range(1, 20), sse)
    plt.xticks(range(1, 20))
    plt.xlabel("Number of Clusters")
    plt.ylabel("SSE")
    plt.show()
