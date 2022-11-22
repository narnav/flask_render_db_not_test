from flask_sqlalchemy import SQLAlchemy
from project import app
from project.models import Client, Book, Log

db = SQLAlchemy(app)
with app.app_context():
    db.create_all()

records =[]

client1 = Client('Amy', 'Paris', 26)
client2 = Client('Bob', 'Berlin', 31)
client3 = Client('Tony', 'Vienna', 17)
client4 = Client('Elenor', 'Madrid', 24)
client5 = Client('Sam', 'Huston', 50)
client6 = Client('Robert', 'London', 42)
client7 = Client('Lisa', 'Amsterdam', 80)


book1 = Book('Green Mile', 'Stephan King', 1996, 3)
book2 = Book('1984', 'George Orwell', 1948, 2)
book3 = Book('Alice in Wonderland', 'Lewis Carroll', 1865, 1)
book4 = Book('I, Robot', 'Isaac Asimov', 1950, 2)
book5 = Book('Fight Club', 'Chuck Palahniuk', 1996, 3)
book6 = Book('The Lord of the Rings', 'J. R. R. Tolkien', 1954, 1)
book7 = Book('Treasure Island', 'Robert Louis Stevenson', 1882, 1)


log1 = Log(1, 5)
log2 = Log(3, 2)
log3 = Log(5, 3)
log4 = Log(3, 5)
log5 = Log(4, 1)
log6 = Log(2, 3)
log7 = Log(1, 4)

i=1
while i <= 7:
    with app.app_context():
        client = f'client{i}'
        book = f'book{i}'
        db.session.add(globals()[client])
        db.session.add(globals()[book])
        db.session.commit()
        i = i + 1
i=1
while i <= 7:
    with app.app_context():
        log = f'log{i}'
        db.session.add(globals()[log])
        db.session.commit()
        i = i + 1


