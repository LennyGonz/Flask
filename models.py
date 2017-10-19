from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

db = SQLAlchemy() # db is a variable it contains a new usable instance of the SQLAlchemy class

# LINES 9 - 15: are the same as the columns for the user table
# so uid, firstname, lastname, email, and pwdhash

class User(db.Model):
  __tablename__ = 'users'
  uid = db.Column(db.Integer, primary_key = True)
  firstname = db.Column(db.String(100))
  lastname = db.Column(db.String(100))
  email = db.Column(db.String(120), unique=True)
  pwdhash = db.Column(db.String(54))

# LINES 30 through 40 we create a constructor to set each of these class atributes
# A couple of things to note about the constructor. The constructor saves the
# firstname and lastname and title case, SO the first letter is capitalized
# It saves the email address in lowercase to make sure that we can match
# regardless of how the user types in his credentials on subsequent sign ins.
# We encrypt the user's passweord right away using the set_password function
# WE THEN STORE THAT ENCRYPTED PASSWORD IN pwdhash
# we use the set password function to set a salted hash of the password instead
# of using a plain text password

  def __init__(self, firstname, lastname, email, password):
    self.firstname = firstname.title() # .title means it'll capitalize...
    self.lastname = lastname.title() # ... the first letter
    self.email = email.lower()  # saves email in all lowercase
    self.set_password(password) # we're encrypting the password

  def set_password(self, password):
    self.pwdhash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.pwdhash, password)

# set_password relies on the function generate_password_hash, which is a
# security function for import from one of Flask's libraries, werkzueg
# That's on line two, where we import that generate_password_hash function
# Lastly, to make everything work together, modify routes.py to look like this
# First import db.init_app to initialize the Flask app for using this database setup
