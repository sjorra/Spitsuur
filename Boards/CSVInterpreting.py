import pandas as pd
def importcsv(file):
    file_path="./Files/"+file
    inputboard=pd.read_csv(file_path)
    return inputboard