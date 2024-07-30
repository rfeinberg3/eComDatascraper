import pandas as pd
from setbuilder import Setbuilder

if __name__ == '__main__':
    
    # Input dir
    data_dir = 'outputs'

    # Build dataset
    list_of_dicts = Setbuilder(data_dir).combine(['itemId', 'title', 'price', 'condition', 'itemDescription'])

    # Truncate and move to pandas DataFrame
    df = pd.DataFrame(list_of_dicts[0:100])

    # Write to csv
    df.to_csv('dataset.csv', sep=',', index=False)