import orm
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import Session

class RETURN:
    OK = 200
    CREATED = 201
    NOT_FOUND = 404

    @staticmethod
    def ok(data):
        return data, RETURN.OK, ""

    @staticmethod
    def not_found(msg):
        return None, RETURN.NOT_FOUND, msg


engine = create_engine('sqlite:///data.db', echo=True)
orm.Base.metadata.create_all(engine)

def get_shops():
    with Session(engine) as session:
        data = []
        for s in session.scalars(select(orm.Shop)).all():
            data.append({'id' : s.id, 'name' : s.name})
        return RETURN.ok(data)

def get_shop(id):
    with Session(engine) as session:
        s = session.scalars(select(orm.Shop).where(orm.Shop.id == id)).one_or_none()
        if s is None:
            return RETURN.not_found("Shop not found")
        data = {'id' : s.id, 'name' : s.name}
        return RETURN.ok(data)

def get_shopping_lists():
    with Session(engine) as session:
        data = []
        for l in session.query(orm.ShoppingList).all():
            data.append({'id' : l.id, 'name' : l.name})
        print(data)
        return data
