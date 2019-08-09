import argparse

from ClusterDistance import calculate_distance
from data import read_categories

parser = argparse.ArgumentParser()

parser.add_argument('name', default='')
parser.add_argument('--data', default='data.csv')

args = parser.parse_args()

data = read_categories(args.data)
cluster_distances = calculate_distance(data, args.name)
for cluster_distance in cluster_distances:
    print(f'{cluster_distance.name}: {cluster_distance.distance}')
