import json
from sqlalchemy.orm import sessionmaker
from models import Publisher, Sale, Shop, Stock, Book


def insert_data(engine):
    Session = sessionmaker(bind=engine)
    session = Session()

    with open('data.json', 'r') as data_json:
        data = json.load(data_json)

    transcription = {
        'publisher': Publisher,
        'book': Book,
        'shop': Shop,
        'stock': Stock,
        'sale': Sale,
    }

    for datas in data:
        table = transcription[datas['model']]
        session.add(table(id=datas['pk'], **datas['fields']))
    session.commit()
    session.close()


def show_shops_with_publisher(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    p_id = input('Input Publisher name: ')
    subq = session.query(Publisher).filter(Publisher.name.ilike(p_id.lower())).subquery()
    subq2 = session.query(Book).join(subq, Book.id_publisher == subq.c.id).subquery()
    subq3 = session.query(Stock).join(subq2, subq2.c.id == Stock.id_book).subquery()
    subq4 = session.query(Shop).join(subq3, subq3.c.id_shop == Shop.id).all()
    session.commit()
    if subq4:
        print(f'Shops where You can buy books of publisher "{p_id}":')
        for c in subq4:
            print(c)
    else:
        print(f'You can not buy books of "{p_id}" or wrong name')


    session.close()
