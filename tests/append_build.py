import sys
sys.path.append('..')

import json
import pandas as pd
from setbuilder import Setbuilder

if __name__ == '__main__':
    
    # Input dir
    data_dir = 'outputs'

    # Build dataset
    list_of_dicts = Setbuilder(data_dir).combine(['itemId', 'title', 'price', 'condition', 'itemDescription'])

    # Move to pandas DataFrame
    df_new = pd.DataFrame(list_of_dicts)

    # Combine with current dataset.json
    with open('dataset.json', 'r') as f:
        dataset = json.load(f)
    df_cur = pd.DataFrame(dataset)
    original_shape = df_cur.shape

    df = pd.concat([df_new, df_cur], ignore_index=True) # Index needs to be reset for proper concatenation

    # Remove duplicates on itemId and title
    df = df.drop_duplicates(subset=['itemId'], keep='first')
    #df = df.drop_duplicates(subset=['title'], keep='first')

    # Remove columns that are obviously low quality
    #TODO Add regex to this section for efficiency
    mask = df['title'].apply(lambda x: x.lower().startswith('test'))
    df = df[~mask]
    df = df.reset_index(drop=True)

    print("Rows added = ", df.shape[0] - original_shape[0], sep="")

    # Write to json
    with open('dataset.json', 'w') as f:
        result = df.to_json(orient='columns', indent=True)
        parsed = json.loads(result)
        json.dump(parsed, f, indent=1)