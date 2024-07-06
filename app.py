from flask import Flask, request, jsonify
import storage

app = Flask(__name__)


# urls
# GET /shops                                    all shops
# GET /shops/{id}                               one shop
# POST /shops                                   create new shop
# PUT /shops/{id}                               update shop
# DELETE /shops/{id}                            delete shop

# GET /products                                 all products
# GET /products/{id}                            one product
# POST /products                                create new product
# PUT /products/{id}                            update product
# DELETE /products/{id}                         delete product
# GET /products/{id}/brands                     all brands
# GET /products/{id}/brands/{brand_id}          one brand
# POST /products/{id}/brands                    add brand
# PUT /products/{id}/brands/{brand_id}          update brand
# DELETE /products/{id}/brands/{brand_id}       delete brand

# GET /storages                                 all storages
# GET /storages/{id}                            one storage
# POST /storages                                create new storage
# PUT /storages/{id}                            update storage
# DELETE /storages/{id}                         delete storage
# GET /storages/{id}/entries                    all entries
# GET /storages/{id}/entries/{entry_id}         one entry
# POST /storages/{id}/entries                   add entry
# PUT /storages/{id}/entries/{entry_id}         update entry
# DELETE /storages/{id}/entries/{entry_id}      delete entry
# PUT /storages/{id}/entries/{entry_id}/move    move entry

# GET /lists                                    all lists
# GET /lists/{id}                               one list
# POST /lists                                   create new list
# PUT /lists/{id}                               update list
# DELETE /lists/{id}                            delete list
# GET /lists/{id}/entries                       all entries
# GET /lists/{id}/entries/{entry_id}            one entry
# POST /lists/{id}/entries                      add entry
# PUT /lists/{id}/entries/{entry_id}            update entry
# DELETE /lists/{id}/entries/{entry_id}         delete entry
# PUT /lists/{id}/entries/{entry_id}/move       move entry

@app.route('/shops', methods=['GET'])
def get_shops():
    return storage.Shops.all()

@app.route('/shops/<int:id>', methods=['GET'])
def get_shop(id):
    return storage.Shops.get(id)

@app.route('/shops', methods=['POST'])
def create_shop():
    input = request.get_json()
    return storage.Shops.create(input)

@app.route('/shops/<int:id>', methods=['PUT'])
def update_shop(id):
    input = request.get_json()
    return storage.Shops.update(id, input)

@app.route('/shops/<int:id>', methods=['DELETE'])
def delete_shop(id):
    return storage.Shops.delete(id)

@app.route('/products', methods=['GET'])
def get_products():
    return storage.Products.all()

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    return storage.Products.get(id)

@app.route('/products', methods=['POST'])
def create_product():
    input = request.get_json()
    return storage.Products.create(input)

@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    input = request.get_json()
    return storage.Products.update(id, input)

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    return storage.Products.delete(id)

@app.route('/products/<int:id>/brands', methods=['GET'])
def get_product_brands(id):
    return storage.Brands.all(id)

@app.route('/products/<int:id>/brands/<int:brand_id>', methods=['GET'])
def get_product_brand(id, brand_id):
    return storage.Brands.get(id, brand_id)

@app.route('/products/<int:id>/brands', methods=['POST'])
def create_product_brand(id):
    input = request.get_json()
    return storage.Brands.create(id, input)

@app.route('/products/<int:id>/brands/<int:brand_id>', methods=['PUT'])
def update_product_brand(id, brand_id):
    input = request.get_json()
    return storage.Brands.update(id, brand_id, input)

@app.route('/products/<int:id>/brands/<int:brand_id>', methods=['DELETE'])
def delete_product_brand(id, brand_id):
    return storage.Brands.delete(id, brand_id)

if __name__ == '__main__':
    app.run()

