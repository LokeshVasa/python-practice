import json

def add_rec(rec):
    with open('db.json', 'r') as file:
        json.dump(data, file)