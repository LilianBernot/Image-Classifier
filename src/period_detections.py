import os
from read_image import get_datetime_image
from utils_dates import convert_str_to_datetime
import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from datetime import timedelta, datetime
from test_data import generate_random_dates

def cluster_dates(dates: list[datetime]) -> dict:
    """
    This function applies a DBSCAN, using on the list of given dates.
    It returns the computed clusters.
    """
    # Convert to timestamps
    timestamps = np.array([date.timestamp() for date in dates]).reshape(-1, 1)  
    
    # eps=86400 for 1-day threshold
    clustering = DBSCAN(eps=86400, min_samples=3).fit(timestamps) 
    labels = clustering.labels_

    # Group dates by cluster
    clusters = {}
    for label, date in zip(labels, dates):
        if label not in clusters:
            clusters[label] = []
        clusters[label].append(date)

    return clusters

def plot_clusters(dates, clusters):
    """
    This function plots the given dates and clusters from the DBSCAN.
    """
    # Create a histogram of the dates
    plt.figure(figsize=(12, 6))
    dates_sorted = sorted(dates)
    bin_edges = [dates_sorted[0] + timedelta(days=i) for i in range((dates_sorted[-1] - dates_sorted[0]).days + 1)]
    plt.hist(dates, bins=bin_edges, color='skyblue', alpha=0.7, label='Date Histogram')

    # Overlay cluster boundaries
    for cluster_label, cluster_dates in clusters.items():
        if cluster_label == -1:  # Noise
            continue
        cluster_start = min(cluster_dates)
        cluster_end = max(cluster_dates)
        plt.axvspan(cluster_start, cluster_end, color='orange', alpha=0.3, label=f'Cluster {cluster_label}')

    # Formatting
    plt.xlabel('Date')
    plt.ylabel('Frequency')
    plt.title('Dates Histogram with DBSCAN Clusters')
    plt.legend()
    plt.grid()
    plt.show()


def plot_dates_clusters(folder_path: str):
    """
    This function plots the DBSCAN of dates from a given folder.
    """
    dates = []
    for image_name in os.listdir(folder_path):
        image_path = os.path.join(folder_path, image_name)
        if os.path.isfile(image_path) and not image_path[-4:]  in ['.txt', '.mp4']:
            dates.append(convert_str_to_datetime(get_datetime_image(image_path)))

    clusters = cluster_dates(dates)
    plot_clusters(dates, clusters)

def plot_test_dates_clusters():
    """
    This function plots the DBSCAN of dates from test data.
    """
    dates = generate_random_dates()
    clusters = cluster_dates(dates)
    plot_clusters(dates, clusters)


plot_test_dates_clusters()