import json

def get_products():
    with open('./products.json','r') as jsonfile:
        file_data = json.loads(jsonfile.read())

    return file_data