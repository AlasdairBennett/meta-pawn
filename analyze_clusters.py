import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pickle

if __name__ == '__main__':
    print("running...")
    pd.set_option('display.max_columns', 20)
    pd.set_option('display.max_rows', 20)
    pd.set_option('display.width', 10000)
    kmeans = pickle.load(open("project/static/model/kmeans_model.pkl", "rb"))
    openings = pd.read_csv('project/static/openings.csv')
    openings = openings.assign(cluster=kmeans.labels_)

    print(openings)
