import pandas as pd


def read_file(filename):
    df = pd.read_excel(filename, 0, 0)
    data = []
    for x in df.itertuples():
        data.append((x[2], x[1], x[3]))
        
    print(data)
    return data