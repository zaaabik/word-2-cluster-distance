from typing import List, Dict


class CategoryDistance:
    def __init__(self, name, distance):
        self.distance = distance
        self.name = name


def levenshtein_distance(a, b):
    n, m = len(a), len(b)
    if n > m:
        a, b = b, a
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if a[j - 1] != b[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]


def calculate_distance(cluster: Dict[str, List[str]], text) -> List[CategoryDistance]:
    distances = []
    for name, items in cluster.items():
        cluster_distance = 0
        for item in items:
            cluster_distance += (levenshtein_distance(item, text) / max(len(text), len(item)))
        cluster_distance /= len(items)
        distances.append(CategoryDistance(name, cluster_distance))

    return distances
