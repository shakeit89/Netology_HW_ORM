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


def print_publisher_by_id(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        p_id = int(input('Введите id издателя: '))
    except ValueError:
        print('Введите натуральное число!')
        return
    a = session.query(Publisher).filter(Publisher.id == p_id).first()
    session.commit()
    if a:
        print(a)
    else:
        print('Издателя с данным id не существует')
    session.close()
