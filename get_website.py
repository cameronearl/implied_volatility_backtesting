import requests
import json
import pandas as pd

url_base = "http://openinsider.com/search?q="
ticker = "ASA"

def create_url(ticker):
    return(url_base+ticker)

url = create_url(ticker)
print(url)

def request_body_txt(url):
    response = requests.get(url)
    body = response.text
    return(body)

a = request_body_txt(create_url("ASA"))
#print(a)

# Read HTML tables into a list of DataFrames
dfs = pd.read_html(a)

# Assume the first table is the one we want
df = dfs[1]

# Convert the DataFrame to a JSON string in 'records' format (list of objects)
json_result = df.to_json(orient='records', indent=4)

print(json_result)