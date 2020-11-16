# from flask_sqlalchemy import SQLAlchemy
# app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products2.db'

# # Database Initialise
# db = SQLAlchemy(app)
# conn = sqlite3.connect('products2.db')

# DB model
# class Products(db.Model):
# 	id = db.Coloumn(db.Integer, primary_key=True)
# 	name = db.Coloumn(db.String(200), nullable=False)
# 	price = db.Coloumn(db.Float(10), nullable=False)
# # Create a function to return a string
# 	def __repr__(self):
# 		return '<Name %r>' % self.id


# # create a cursor
# c = conn.cursor()
# # create a table
# c.execute("""CREATE TABLE products (

# 		Product TEXT,
# 		Price REAL

# 		)""")


# conn.commit()
# conn.close()


# sqlite3/flask documentation
# DATABASE = 'products.db'

# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect(DATABASE)
#     return db

# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()

