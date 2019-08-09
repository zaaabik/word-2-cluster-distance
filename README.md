# word-2-cluster-distance

Simple program to calculate distance between word and cluster of words

python version **python3+**

run examples:
* ```python main.py "шоколадка топовая"```
* ```python main.py "невкусная колбаса"```
* ```python main.py "невкусная колбаса" --data custom_data.csv```

If you want to add new data, add new row in csv file  
!!!only two columns are required!!!
1. Category (product category name)
1. Name (name of product)

# Run tests
```python -m unittest discover -s test```
