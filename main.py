# import sqlite3
#
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()

# cursor.execute("create table books (id integer primary key, title varchar(250) NOT NULL,"
#                "author varchar(250) not null, rating float not null)")

# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.name}>'
#
# db.create_all()
#
# book1= Books(name="Harry Potter", author="J.K. Rowling", rating=9.8)
# db.session.add(book1)
# db.session.commit()

# book = Books.query.filter_by(name="Harry Potter").first()
# book.name = "Harry Potter and The Chamber of Secrets"
# db.session.commit()
# print(book)

delete_boook = Books.query.get(1)
db.session.delete(delete_boook)
print(delete_boook)
db.session.commit()