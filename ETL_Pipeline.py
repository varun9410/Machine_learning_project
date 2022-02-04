import pymongo
import json
import pandas as pd
import datetime
def Extract(API_key,out_file):
    client = pymongo.MongoClient(Api_key)
    db = client["database"]
    col = db["Sales"] 
    x = col.find()
    for data in x:
        json.dump(x, out_file)
    return str(out_file)
def transform(out_file):
    with open('persons.json') as f:
        data = json.load(f)
    transformed = []
    for user in data:
        transformed.append({
            'ID': user['id'],
            'Name': user['name'],
            'Username': user['username'],
            'Email': user['email'],
            'Address': f"{user['address']['street']}, {user['address']['suite']}, {user['address']['city']}",
            'PhoneNumber': user['phone'],
            'Produc': user['Product']['name']
        })
    return pd.DataFrame(transformed)
def load(data: pd.DataFrame, path: str) -> None:
    data.to_csv(path_or_buf=path, index=False)

if __name__ == '__main__':
    Api_key=""
    data = Extract(Api_key)
    df_users = transform(data)
    load(data=df_users, path=f'data/users_{int(datetime.now().timestamp())}.csv')