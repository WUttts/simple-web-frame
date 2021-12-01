import pandas as pd

def read_file(filename):
    df = pd.read_excel(filename)
    print(df)
    