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
    def all():
        with Session(engine) as session:
            data = []
            for s in session.scalars(select(orm.Shop)).all():
                data.append({'id' : s.id, 'name' : s.name})
            return RETURN.ok(data)

    def get(id):
        with Session(engine) as session:
            s = session.scalars(select(orm.Shop).where(orm.Shop.id == id)).one_or_none()
            if s is None:
                return RETURN.not_found("Shop not found")
            data = {'id' : s.id, 'name' : s.name}
            return RETURN.ok(data)

    def create(input):
        if 'name' not in input:
            return RETURN.bad_request("Missing name")
        with Session(engine) as session:
            s = orm.Shop(name=input['name'])
            session.add(s)
            session.commit()
            return RETURN.created({'id' : s.id, 'name' : s.name})

    def update(id, input):
        with Session(engine) as session:
            s = session.scalars(select(orm.Shop).where(orm.Shop.id == id)).one_or_none()
            if s is None:
                return RETURN.not_found("Shop not found")
            if 'name' in input:
                s.name = input['name']
            session.commit()
            return RETURN.ok({'id' : s.id, 'name' : s.name})

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
    def all():
        with Session(engine) as session:
            data = []
            for p in session.scalars(select(orm.Product)).all():
                data.append({'id' : p.id, 'name' : p.name, 'unit' : p.unit})
            return RETURN.ok(data)

    @staticmethod
    def get(id):
        with Session(engine) as session:
            p = session.scalars(select(orm.Product).where(orm.Product.id == id)).one_or_none()
            if p is None:
                return RETURN.not_found("Product not found")
            data = {'id' : p.id, 'name' : p.name, 'unit' : p.unit}
            return RETURN.ok(data)

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
            return RETURN.created({'id' : p.id, 'name' : p.name, 'unit' : p.unit})

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
            return RETURN.ok({'id' : p.id, 'name' : p.name, 'unit' : p.unit})

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
    def all(product_id):
        with Session(engine) as session:
            data = []
            for b in session.scalars(select(orm.BrandedProduct).where(orm.BrandedProduct.product_id == product_id)).all():
                data.append({'id' : b.id, 'product_id' : b.product_id, 'name' : b.name})
            return RETURN.ok(data)

    @staticmethod
    def get(product_id, id):
        with Session(engine) as session:
            b = session.scalars(select(orm.BrandedProduct).where(orm.BrandedProduct.product_id == product_id).where(orm.BrandedProduct.id == id)).one_or_none()
            if b is None:
                return RETURN.not_found("Brand not found")
            data = {'id' : b.id, 'product_id' : b.product_id, 'name' : b.name}
            return RETURN.ok(data)

    @staticmethod
    def create(product_id, input):
        if 'name' not in input:
            return RETURN.bad_request("Missing name")
        with Session(engine) as session:
            b = orm.BrandedProduct(product_id=product_id, name=input['name'])
            session.add(b)
            session.commit()
            return RETURN.created({'id' : b.id, 'product_id' : b.product_id, 'name' : b.name})

    @staticmethod
    def update(product_id, id, input):
        with Session(engine) as session:
            b = session.scalars(select(orm.BrandedProduct).where(orm.BrandedProduct.product_id == product_id).where(orm.BrandedProduct.id == id)).one_or_none()
            if b is None:
                return RETURN.not_found("Brand not found")
            if 'name' in input:
                b.name = input['name']
            session.commit()
            return RETURN.ok({'id' : b.id, 'product_id' : b.product_id, 'name' : b.name})

    @staticmethod
    def delete(product_id, id):
        with Session(engine) as session:
            b = session.scalars(select(orm.BrandedProduct).where(orm.BrandedProduct.product_id == product_id).where(orm.BrandedProduct.id == id)).one_or_none()
            if b is None:
                return RETURN.not_found("Brand not found")
            session.delete(b)
            session.commit()
            return RETURN.no_content()

def get_shopping_lists():
    with Session(engine) as session:
        data = []
        for l in session.query(orm.ShoppingList).all():
            data.append({'id' : l.id, 'name' : l.name})
        print(data)
        return data
