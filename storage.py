import orm
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


engine = create_engine('sqlite:///data.db', echo=True)
orm.Base.metadata.create_all(engine)

def get_shopping_lists():
    with Session(engine) as session:
        data = []
        for l in session.query(orm.ShoppingList).all():
            data.append({'id' : l.id, 'name' : l.name})
        print(data)
        return data
