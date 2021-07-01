import json

def get_products():
    f = open('products.json')
    products  = json.load(f)
    f.close()
    return products