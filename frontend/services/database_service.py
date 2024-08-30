import json
import pandas as pd

def get_data():
    # connect to the database
    # for now, we will just read the data from a json file
    # read json
    with open('D:\\datathon_2024\\factored-datathon-2024-sanima\\frontend\\test\\data.json', 'r') as f:
        data = json.load(f)
    return data