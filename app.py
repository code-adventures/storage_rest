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

@app.route('/shops', methods=['GET', 'POST'])
def get_shops():
    if request.method == 'GET':
        return storage.Shops.all()
    input = request.get_json()
    return storage.Shops.create(input)
    

@app.route('/shops/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_shop(id):
    if request.method == 'GET':
        return storage.Shops.get(id)
    if request.method == 'PUT':
        input = request.get_json()
        return storage.Shops.update(id, input)
    return storage.Shops.delete(id)

@app.route('/products', methods=['GET', 'POST'])
def get_products():
    if request.method == 'GET':
        return storage.Products.all()
    input = request.get_json()
    return storage.Products.create(input)

@app.route('/products/<int:id>', methods=['GET','PUT','DELETE'])
def get_product(id):
    if request.method == 'GET':
        return storage.Products.get(id)
    if request.method == 'PUT':
        input = request.get_json()
        return storage.Products.update(id, input)
    return storage.Products.delete(id)

@app.route('/products/<int:id>/brands', methods=['GET', 'POST'])
def get_product_brands(id):
    if request.method == 'GET':
        return storage.Brands.all(id)
    input = request.get_json()
    return storage.Brands.create(id, input)

@app.route('/products/<int:id>/brands/<int:brand_id>', methods=['GET','PUT','DELETE'])
def get_product_brand(id, brand_id):
    if request.method == 'GET':
        return storage.Brands.get(id, brand_id)
    if request.method == 'PUT':
        input = request.get_json()
        return storage.Brands.update(id, brand_id, input)
    return storage.Brands.delete(id, brand_id)

@app.route('/storages', methods=['GET', 'POST'])
def get_storages():
    if request.method == 'GET':
        return storage.Storages.all()
    input = request.get_json()
    return storage.Storages.create(input)

@app.route('/storages/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_storage(id):
    if request.method == 'GET':
        return storage.Storages.get(id)
    if request.method == 'PUT':
        input = request.get_json()
        return storage.Storages.update(id, input)
    return storage.Storages.delete(id)

@app.route('/storages/<int:id>/entries', methods=['GET', 'POST'])
def get_storage_entries(id):
    if request.method == 'GET':
        return storage.ShoppingLists.all()
    input = request.get_json()
    return storage.ShoppingLists.create(input)

@app.route('/storages/<int:id>/entries/<int:entry_id>', methods=['GET','PUT','DELETE'])
def get_storage_entry(id, entry_id):
    if request.method == 'GET':
        return storage.ShoppingLists.get(id, entry_id)
    if request.method == 'PUT':
        input = request.get_json()
        return storage.ShoppingLists.update(id, entry_id, input)
    return storage.ShoppingLists.delete(id, entry_id)

@app.route('/storages/<int:id>/entries/<int:entry_id>/move', methods=['PUT'])
def move_storage_entry(id, entry_id):
    return "", 404

@app.route('/lists', methods=['GET', 'POST'])
def get_lists():
    if request.method == 'GET':
        return storage.ShoppingLists.all()
    input = request.get_json()
    return storage.ShoppingLists.create(input)

@app.route('/lists/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_list(id):
    if request.method == 'GET':
        return storage.ShoppingLists.get(id)
    if request.method == 'PUT':
        input = request.get_json()
        return storage.ShoppingLists.update(id, input)
    return storage.ShoppingLists.delete(id)

@app.route('/lists/<int:id>/entries', methods=['GET', 'POST'])
def get_list_entries(id):
    if request.method == 'GET':
        return storage.ShoppingLists.all()
    input = request.get_json()
    return storage.ShoppingLists.create(id, input)

@app.route('/lists/<int:id>/entries/<int:entry_id>', methods=['GET','PUT','DELETE'])
def get_list_entry(id, entry_id):
    if request.method == 'GET':
        return storage.ShoppingLists.get(id, entry_id)
    if request.method == 'PUT':
        input = request.get_json()
        return storage.ShoppingLists.update(id, entry_id, input)
    return storage.ShoppingLists.delete(id, entry_id)

@app.route('/lists/<int:id>/entries/<int:entry_id>/move', methods=['PUT'])
def move_list_entry(id, entry_id):
    return "", 404

if __name__ == '__main__':
    app.run()

