import pickle
import matplotlib.pyplot as plt
import pandas as pd
from kneed import KneeLocator
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def train_model(data_set):
    # normalize the features
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(data_set)

    # try different number of clusters
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

    # plot the squared sum error by number of cluster
    plt.plot(range(1, 21), sse)
    plt.xticks(range(1, 21))
    plt.xlabel("Number of Clusters")
    plt.ylabel("SSE")
    plt.show()

    # locate the knee
    kl = KneeLocator(range(1, 21), sse, curve="convex", direction="decreasing")
    n = kl.elbow

    # train the models using the optimal n_cluster
    kmeans = KMeans(n_clusters=n)
    kmeans.fit(scaled_features)

    return kmeans


# this script trains the models and pickle it to project/static/models/
if __name__ == '__main__':
    print("running...")
    pd.set_option('display.max_columns', 20)
    pd.set_option('display.max_rows', 20)
    pd.set_option('display.width', 10000)
    openings = pd.read_csv('project/static/openings.csv')
    openings_features = openings.drop(['opening_eco', 'opening_name'], axis=1)
    # removing novel openings
    openings_features = openings_features[openings_features['n_games_played'] >= 10]

    w_data_set = openings_features[openings_features['w_win_rate'] >= openings_features['b_win_rate']]
    b_data_set = openings_features[openings_features['w_win_rate'] <= openings_features['b_win_rate']]

    w_model = train_model(w_data_set)
    b_model = train_model(b_data_set)

    # pickle the models
    pickle.dump(w_model, open("project/static/models/w_model.pkl", "wb"))
    pickle.dump(b_model, open("project/static/models/b_model.pkl", "wb"))
