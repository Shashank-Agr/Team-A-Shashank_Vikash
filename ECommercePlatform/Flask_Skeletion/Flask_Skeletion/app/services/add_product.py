import json

def add_to_cart(product_id):
    with open('./products.json','r') as jsonfile:
        file_data = json.loads(jsonfile.read())
    for x in file_data:
        if x["sku"]==product_id:
            #x['count'] = 1
            return x
    return {}