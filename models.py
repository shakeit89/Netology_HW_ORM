import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=50), unique=True)

    def __str__(self):
        str_books = ''
        for i in self.books:
            str_books += f'\n{i}'
        return f'Publisher  id :{self.id}. Publisher name: {self.name}.' \
               f'\nBooks of publisher: {str_books}'


class Book(Base):
    __tablename__ = 'book'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=50), nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable=False)
    publisher = relationship(Publisher, backref='books')

    def __str__(self):
        return f'Book id: {self.id}. Book Title: "{self.title}". Publisher name: "{self.publisher.name}"'




class Shop(Base):
    __tablename__ = 'shop'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=50), unique=True)

    def __str__(self):
        return f'Shop  {self.id}: {self.name}'


class Stock(Base):
    __tablename__ = 'stock'

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    books = relationship(Book, backref='stocks')
    shops = relationship(Shop, backref='stocks')

    def __str__(self):
        return f'Stock  {self.id}: Book: {self.id_book}. Shop: {self.id_shop}. Count: {self.count}'


class Sale(Base):
    __tablename__ = 'sale'

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float, nullable=False)
    date_sale = sq.Column(sq.Date, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    stocks = relationship(Stock, backref='sales')

    def __str__(self):
        return f'Sales  {self.id}: Price: {self.price}. Data sale: {self.date_sale}. ' \
               f'Stock:  {self.id_stock}. Count: {self.count} '


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
