from flask import Flask
from flask import jsonify
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
    data, code, code_msg = storage.get_shops()
    if data:
        return jsonify(data), code
    return code_msg, code

@app.route('/shops/<int:id>', methods=['GET'])
def get_shop(id):
    data, code, code_msg = storage.get_shop(id)
    if data:
        return jsonify(data), code
    return code_msg, code

@app.route('/shops', methods=['POST'])
def create_shop():
    data, code, code_msg = storage.create_shop()
    if data:
        return jsonify(data), code
    return code_msg, code

@app.route('/shops/<int:id>', methods=['PUT'])
def update_shop(id):
    data, code, code_msg = storage.update_shop(id)
    if data:
        return jsonify(data), code
    return code_msg, code

@app.route('/shops/<int:id>', methods=['DELETE'])
def delete_shop(id):
    data, code, code_msg = storage.delete_shop(id)
    if data:
        return jsonify(data), code
    return code_msg, code


@app.route('/')
def hello_world():
    return jsonify(storage.get_shopping_lists())

if __name__ == '__main__':
    app.run()

