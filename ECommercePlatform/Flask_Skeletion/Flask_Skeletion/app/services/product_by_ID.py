#TO complete

import json

def get_product_by_id(product_id):
    with open('./products.json','r') as jsonfile:
        file_data = json.loads(jsonfile.read())

    product = list()
    for x in file_data:
        for pid in x['category']:
            if pid['id'] == product_id:
                product.append(x)
    return product    