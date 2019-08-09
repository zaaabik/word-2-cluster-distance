import pandas as pd

CategoryColumn = 'Category'
NameColumn = 'Name'


def read_categories(path):
    data = pd.read_csv(path)
    data[CategoryColumn].apply(lambda x: x.lower())
    data = data.groupby(CategoryColumn)
    return dict(tuple(data[NameColumn]))
