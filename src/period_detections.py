import os
from read_image import get_datetime_image
from utils_dates import convert_str_to_datetime
import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from datetime import timedelta, datetime
from utils.user_input import ask_user
from create_template import create_template_file, update_template_file

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

def get_cluster_periods(clusters):
    """
    Gets the cluster periods by computing min and max dates.
    Returns : tuple (label, start, end)
    """
    cluster_periods: list[tuple[int, datetime, datetime]] = []
    for cluster_label, cluster_dates in clusters.items():
        if cluster_label == -1:  # Noise
            continue
        cluster_start = min(cluster_dates)
        cluster_end = max(cluster_dates)
        cluster_periods.append((cluster_label, cluster_start, cluster_end))

    return cluster_periods

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
    cluster_periods = get_cluster_periods(clusters=clusters)
    for label, start, end in cluster_periods:
        plt.axvspan(start, end, color='orange', alpha=0.3, label=f'Cluster {label}') # type: ignore

    # Formatting
    plt.xlabel('Date')
    plt.ylabel('Frequency')
    plt.title('Dates Histogram with DBSCAN Clusters')
    plt.legend()
    plt.grid()
    plt.show()


def user_accepts_suggestion(root_folder:str, period_suggestions:str):
    """
    Asks the user to accept or not the offered suggestions.
    If accepts, it updates the periods file with the given suggestions.
    """
    if ask_user():
        print("You accepted the changes, we updated your periods.txt file :")

        create_template_file(root_folder=root_folder)

        update_template_file(root_folder=root_folder, content=period_suggestions)


def print_period_suggestion(clusters) -> str:
    """
    Prints period suggestion out of the given clusters.

    Returns :
        - The detected periods formatted in strings
    """
    cluster_periods = get_cluster_periods(clusters=clusters)
    suggested_periods = ""
    for label, start, end in cluster_periods:
        suggested_periods += start.strftime('%Y-%m-%d') + ' to ' + end.strftime('%Y-%m-%d') + '\n'

    print("\n--- Suggested cluster periods : ---\n")
    print(suggested_periods)
    print("-------------------------------------\n")

    return suggested_periods


def get_period_suggestion(root_folder):
    """
    Plots cluster dates and gives suggestion to the user.
    """
    dates = []
    for image_name in os.listdir(root_folder):
        image_path = os.path.join(root_folder, image_name)
        if os.path.isfile(image_path) and not image_path[-4:]  in ['.txt', '.mp4']:
            dates.append(convert_str_to_datetime(get_datetime_image(image_path)))

    clusters = cluster_dates(dates)

    period_suggestions = print_period_suggestion(clusters=clusters)

    plot_clusters(dates, clusters)

    user_accepts_suggestion(root_folder, period_suggestions)


if __name__ == "__main__":
    import sys

    get_period_suggestion(sys.argv[1])