from flask import Flask, request, jsonify, send_from_directory
import storage

app = Flask(__name__)


# GET /shops                                    all shops
# GET /shops/{id}                               one shop
# POST /shops                                   create new shop
# PUT /shops/{id}                               update shop
# DELETE /shops/{id}                            delete shop
# GET /shops/{id}/pic                           shop picture
# POST /shops/{id}/pic                          add shop picture
# PUT /shops/{id}/pic                           update shop picture
# DELETE /shops/{id}/pic                        delete shop picture

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
# GET /products/{id}/brands/{brand_id}/pic      brand picture
# POST /products/{id}/brands/{brand_id}/pic     add brand picture
# PUT /products/{id}/brands/{brand_id}/pic      update brand picture
# DELETE /products/{id}/brands/{brand_id}/pic   delete brand picture

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
# POST /storages/{id}/entries/{entry_id}/move   move entry

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
# POST /lists/{id}/entries/{entry_id}/move      move entry

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

@app.route('/shops/<int:id>/pic', methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_shop_pic(id):
    if request.method == 'GET':
        data, ret = storage.Shops.get_pic(id)
        if ret == 200:
            return send_from_directory('static/pic', data[0], mimetype=data[1])
        return data, ret
    if request.method == 'POST':
        return storage.Shops.add_pic(id, request.content_type, request.data)
    if request.method == 'PUT':
        return storage.Shops.update_pic(id, request.content_type, request.data)
    return storage.Shops.delete_pic(id)

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

@app.route('/storages/<int:id>/entries/<int:entry_id>/move', methods=['POST'])
def move_storage_entry(id, entry_id):
    input = request.get_json()
    return storage.StorageEntries.move(id, entry_id, input)

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
        return storage.ShoppingEntries.all(id)
    input = request.get_json()
    return storage.ShoppingEntries.create(id, input)

@app.route('/lists/<int:id>/entries/<int:entry_id>', methods=['GET','PUT','DELETE'])
def get_list_entry(id, entry_id):
    if request.method == 'GET':
        return storage.ShoppingEntries.get(id, entry_id)
    if request.method == 'PUT':
        input = request.get_json()
        return storage.ShoppingEntries.update(id, entry_id, input)
    return storage.ShoppingEntries.delete(id, entry_id)

@app.route('/lists/<int:id>/entries/<int:entry_id>/move', methods=['POST'])
def move_list_entry(id, entry_id):
    input = request.get_json()
    return storage.ShoppingEntries.move(id, entry_id, input)

if __name__ == '__main__':
    app.run()

