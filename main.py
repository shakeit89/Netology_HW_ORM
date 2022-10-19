import sqlalchemy
import configparser
from models import create_tables, Publisher, Sale, Shop, Stock, Book
from db_func import insert_data, show_shops_with_publisher

if __name__ == '__main__':
    # извлекаем данные из config.ini
    config = configparser.ConfigParser()
    config.read('config.ini')
    db_name, user = config['Database']['name'], config['Database']['login']
    password, ip = config['Database']['password'], config['Database']['ip']

    DSN = f'postgresql://{user}:{password}@{ip}/{db_name}'
    engine = sqlalchemy.create_engine(DSN)

    # cоздаем таблицы
    create_tables(engine)

    # загружаем данные в таблицу из data.json
    insert_data(engine=engine)

    # выводим издателя по id
    show_shops_with_publisher(engine=engine)
