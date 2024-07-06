import orm
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import Session

class RETURN:
    OK = 200
    CREATED = 201
    NO_CONTENT = 204
    BAD_REQUEST = 400
    NOT_FOUND = 404

    @staticmethod
    def ok(data):
        return data, RETURN.OK

    @staticmethod
    def created(data):
        return data, RETURN.CREATED

    @staticmethod
    def no_content():
        return "", RETURN.NO_CONTENT

    @staticmethod
    def not_found(msg):
        return msg, RETURN.NOT_FOUND

    @staticmethod
    def bad_request(msg):
        return msg, RETURN.BAD_REQUEST


engine = create_engine('sqlite:///data.db', echo=True)
orm.Base.metadata.create_all(engine)

class Shops:
    @staticmethod
    def object_to_dict(obj):
        return {'url' : f'/shops/{obj.id}', 'name' : obj.name}

    @staticmethod
    def all():
        with Session(engine) as session:
            data = []
            for s in session.scalars(select(orm.Shop)).all():
                data.append(Shops.object_to_dict(s))
            return RETURN.ok(data)

    @staticmethod
    def get(id):
        with Session(engine) as session:
            s = session.scalars(select(orm.Shop).where(orm.Shop.id == id)).one_or_none()
            if s is None:
                return RETURN.not_found("Shop not found")
            return RETURN.ok(Shops.object_to_dict(s))

    @staticmethod
    def create(input):
        if 'name' not in input:
            return RETURN.bad_request("Missing name")
        with Session(engine) as session:
            s = orm.Shop(name=input['name'])
            session.add(s)
            session.commit()
            return RETURN.created(Shops.object_to_dict(s))

    @staticmethod
    def update(id, input):
        with Session(engine) as session:
            s = session.scalars(select(orm.Shop).where(orm.Shop.id == id)).one_or_none()
            if s is None:
                return RETURN.not_found("Shop not found")
            if 'name' in input:
                s.name = input['name']
            session.commit()
            return RETURN.ok(Shops.object_to_dict(s))

    @staticmethod
    def delete(id):
        with Session(engine) as session:
            s = session.scalars(select(orm.Shop).where(orm.Shop.id == id)).one_or_none()
            if s is None:
                return RETURN.not_found("Shop not found")
            session.delete(s)
            session.commit()
            return RETURN.no_content()


class Products:
    @staticmethod
    def object_to_dict(obj):
        return {'url' : f'/products/{obj.id}', 'name' : obj.name, 'unit' : obj.unit}

    @staticmethod
    def all():
        with Session(engine) as session:
            data = []
            for p in session.scalars(select(orm.Product)).all():
                data.append(Products.object_to_dict(p))
            return RETURN.ok(data)

    @staticmethod
    def get(id):
        with Session(engine) as session:
            p = session.scalars(select(orm.Product).where(orm.Product.id == id)).one_or_none()
            if p is None:
                return RETURN.not_found("Product not found")
            return RETURN.ok(Products.object_to_dict(p))

    @staticmethod
    def create(input):
        if 'name' not in input:
            return RETURN.bad_request("Missing name")
        if 'unit' not in input:
            return RETURN.bad_request("Missing unit")
        with Session(engine) as session:
            p = orm.Product(name=input['name'], unit=input['unit'])
            session.add(p)
            session.commit()
            return RETURN.created(Products.object_to_dict(p))

    @staticmethod
    def update(id, input):
        with Session(engine) as session:
            p = session.scalars(select(orm.Product).where(orm.Product.id == id)).one_or_none()
            if p is None:
                return RETURN.not_found("Product not found")
            if 'name' in input:
                p.name = input['name']
            if 'unit' in input:
                p.unit = input['unit']
            session.commit()
            return RETURN.ok(Products.object_to_dict(p))

    @staticmethod
    def delete(id):
        with Session(engine) as session:
            p = session.scalars(select(orm.Product).where(orm.Product.id == id)).one_or_none()
            if p is None:
                return RETURN.not_found("Product not found")
            session.delete(p)
            session.commit()
            return RETURN.no_content()

class Brands:
    @staticmethod
    def object_to_dict(obj):
        return {'product_url' : f'/products/{obj.product_id}', 'url' : f'/products/{obj.product_id}/brands/{obj.id}', 'name' : obj.name}

    @staticmethod
    def all(product_id):
        with Session(engine) as session:
            data = []
            for b in session.scalars(select(orm.BrandedProduct).where(orm.BrandedProduct.product_id == product_id)).all():
                data.append(Brands.object_to_dict(b))
            return RETURN.ok(data)

    @staticmethod
    def get(product_id, id):
        with Session(engine) as session:
            b = session.scalars(select(orm.BrandedProduct).where(orm.BrandedProduct.product_id == product_id).where(orm.BrandedProduct.id == id)).one_or_none()
            if b is None:
                return RETURN.not_found("Brand not found")
            return RETURN.ok(Brands.object_to_dict(b))

    @staticmethod
    def create(product_id, input):
        if 'name' not in input:
            return RETURN.bad_request("Missing name")
        with Session(engine) as session:
            b = orm.BrandedProduct(product_id=product_id, name=input['name'])
            session.add(b)
            session.commit()
            return RETURN.created(Brands.object_to_dict(b))

    @staticmethod
    def update(product_id, id, input):
        with Session(engine) as session:
            b = session.scalars(select(orm.BrandedProduct).where(orm.BrandedProduct.product_id == product_id).where(orm.BrandedProduct.id == id)).one_or_none()
            if b is None:
                return RETURN.not_found("Brand not found")
            if 'name' in input:
                b.name = input['name']
            session.commit()
            return RETURN.ok(Brands.object_to_dict(b))

    @staticmethod
    def delete(product_id, id):
        with Session(engine) as session:
            b = session.scalars(select(orm.BrandedProduct).where(orm.BrandedProduct.product_id == product_id).where(orm.BrandedProduct.id == id)).one_or_none()
            if b is None:
                return RETURN.not_found("Brand not found")
            session.delete(b)
            session.commit()
            return RETURN.no_content()

class Storages:
    @staticmethod
    def object_to_dict(obj):
        return {'url' : f'/storages/{obj.id}', 'name' : obj.name}

    @staticmethod
    def all():
        with Session(engine) as session:
            data = []
            for s in session.scalars(select(orm.Storage)).all():
                data.append(Storages.object_to_dict(s))
            return RETURN.ok(data)

    @staticmethod
    def get(id):
        with Session(engine) as session:
            s = session.scalars(select(orm.Storage).where(orm.Storage.id == id)).one_or_none()
            if s is None:
                return RETURN.not_found("Storage not found")
            return RETURN.ok(Storages.object_to_dict(s))

    @staticmethod
    def create(input):
        if 'name' not in input:
            return RETURN.bad_request("Missing name")
        with Session(engine) as session:
            s = orm.Storage(name=input['name'])
            session.add(s)
            session.commit()
            return RETURN.created(Storages.object_to_dict(s))

    @staticmethod
    def update(id, input):
        with Session(engine) as session:
            s = session.scalars(select(orm.Storage).where(orm.Storage.id == id)).one_or_none()
            if s is None:
                return RETURN.not_found("Storage not found")
            if 'name' in input:
                s.name = input['name']
            session.commit()
            return RETURN.ok(Storages.object_to_dict(s))

    @staticmethod
    def delete(id):
        with Session(engine) as session:
            s = session.scalars(select(orm.Storage).where(orm.Storage.id == id)).one_or_none()
            if s is None:
                return RETURN.not_found("Storage not found")
            session.delete(s)
            session.commit()
            return RETURN.no_content()

class StorageEntries:
    @staticmethod
    def object_to_dict(obj):
        return {'url' : f'/storages/{obj.storage_id}/entries/{obj.id}', 'storage_url' : f'/storages/{obj.storage_id}', 'product_url' : f'/products/{obj.product_id}', 'amount' : obj.amount}    

    @staticmethod
    def all(storage_id):
        with Session(engine) as session:
            data = []
            for e in session.scalars(select(orm.StorageEntry).where(orm.StorageEntry.storage_id == storage_id)).all():
                data.append(StorageEntries.object_to_dict(e))
            return RETURN.ok(data)

    @staticmethod
    def get(storage_id, id):
        with Session(engine) as session:
            e = session.scalars(select(orm.StorageEntry).where(orm.StorageEntry.storage_id == storage_id).where(orm.StorageEntry.id == id)).one_or_none()
            if e is None:
                return RETURN.not_found("Entry not found")
            return RETURN.ok(StorageEntries.object_to_dict(e))

    @staticmethod
    def create(storage_id, input):
        if 'product_id' not in input:
            return RETURN.bad_request("Missing product_id")
        if 'amount' not in input:
            return RETURN.bad_request("Missing amount")
        with Session(engine) as session:
            e = orm.StorageEntry(storage_id=storage_id, product_id=input['product_id'], amount=input['amount'])
            session.add(e)
            session.commit()
            return RETURN.created(StorageEntries.object_to_dict(e))

    @staticmethod
    def update(storage_id, id, input):
        with Session(engine) as session:
            e = session.scalars(select(orm.StorageEntry).where(orm.StorageEntry.storage_id == storage_id).where(orm.StorageEntry.id == id)).one_or_none()
            if e is None:
                return RETURN.not_found("Entry not found")
            if 'product_id' in input:
                e.product_id = input['product_id']
            if 'amount' in input:
                e.amount = input['amount']
            session.commit()
            return RETURN.ok(StorageEntries.object_to_dict(e))

    @staticmethod
    def delete(storage_id, id):
        with Session(engine) as session:
            e = session.scalars(select(orm.StorageEntry).where(orm.StorageEntry.storage_id == storage_id).where(orm.StorageEntry.id == id)).one_or_none()
            if e is None:
                return RETURN.not_found("Entry not found")
            session.delete(e)
            session.commit()
            return RETURN.no_content()

class ShoppingLists:
    @staticmethod
    def object_to_dict(obj):
        return {'url' : f'/lists/{obj.id}', 'name' : obj.name}

    @staticmethod
    def all():
        with Session(engine) as session:
            data = []
            for l in session.scalars(select(orm.ShoppingList)).all():
                data.append(ShoppingLists.object_to_dict(l))
            return RETURN.ok(data)

    @staticmethod
    def get(id):
        with Session(engine) as session:
            l = session.scalars(select(orm.ShoppingList).where(orm.ShoppingList.id == id)).one_or_none()
            if l is None:
                return RETURN.not_found("ShoppingList not found")
            return RETURN.ok(ShoppingLists.object_to_dict(l))

    @staticmethod
    def create(input):
        if 'name' not in input:
            return RETURN.bad_request("Missing name")
        with Session(engine) as session:
            l = orm.ShoppingList(name=input['name'])
            session.add(l)
            session.commit()
            return RETURN.created(ShoppingLists.object_to_dict(l))

    @staticmethod
    def update(id, input):
        with Session(engine) as session:
            l = session.scalars(select(orm.ShoppingList).where(orm.ShoppingList.id == id)).one_or_none()
            if l is None:
                return RETURN.not_found("ShoppingList not found")
            if 'name' in input:
                l.name = input['name']
            session.commit()
            return RETURN.ok(ShoppingLists.object_to_dict(l))

    @staticmethod
    def delete(id):
        with Session(engine) as session:
            l = session.scalars(select(orm.ShoppingList).where(orm.ShoppingList.id == id)).one_or_none()
            if l is None:
                return RETURN.not_found("ShoppingList not found")
            session.delete(l)
            session.commit()
            return RETURN.no_content()

class ShoppingEntries:
    @staticmethod
    def object_to_dict(obj):
        return {'url' : f'/lists/{obj.shopping_list_id}/entries/{obj.id}', 'shopping_list_url' : f'/lists/{obj.shopping_list_id}', 'product_url' : f'/products/{obj.product_id}', 'amount' : obj.amount}

    @staticmethod
    def all():
        with Session(engine) as session:
            data = []
            for e in session.scalars(select(orm.ShoppingEntry)).all():
                data.append(ShoppingEntries.object_to_dict(e))
            return RETURN.ok(data)

    @staticmethod
    def get(shopping_list_id, id):
        with Session(engine) as session:
            e = session.scalars(select(orm.ShoppingEntry).where(orm.ShoppingEntry.shopping_list_id == shopping_list_id).where(orm.ShoppingEntry.id == id)).one_or_none()
            if e is None:
                return RETURN.not_found("Entry not found")
            return RETURN.ok(ShoppingEntries.object_to_dict(e))

    @staticmethod
    def create(shopping_list_id, input):
        if 'product_id' not in input:
            return RETURN.bad_request("Missing product_id")
        if 'amount' not in input:
            return RETURN.bad_request("Missing amount")
        with Session(engine) as session:
            e = orm.ShoppingEntry(shopping_list_id=shopping_list_id, product_id=input['product_id'], amount=input['amount'])
            session.add(e)
            session.commit()
            return RETURN.created(ShoppingEntries.object_to_dict(e))

    @staticmethod
    def update(shopping_list_id, id, input):
        with Session(engine) as session:
            e = session.scalars(select(orm.ShoppingEntry).where(orm.ShoppingEntry.shopping_list_id == shopping_list_id).where(orm.ShoppingEntry.id == id)).one_or_none()
            if e is None:
                return RETURN.not_found("Entry not found")
            if 'product_id' in input:
                e.product_id = input['product_id']
            if 'amount' in input:
                e.amount = input['amount']
            session.commit()
            return RETURN.ok(ShoppingEntries.object_to_dict(e))

    @staticmethod
    def delete(shopping_list_id, id):
        with Session(engine) as session:
            e = session.scalars(select(orm.ShoppingEntry).where(orm.ShoppingEntry.shopping_list_id == shopping_list_id).where(orm.ShoppingEntry.id == id)).one_or_none()
            if e is None:
                return RETURN.not_found("Entry not found")
            session.delete(e)
            session.commit()
            return RETURN.no_content()
