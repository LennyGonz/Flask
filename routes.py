from flask import Flask, request, render_template  #YOU HAVE TO ADD THIS TO RENDER TEMPLATES
from forms import SignupForm
from models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgressql: http://127.0.0.1:5000/'
db.init_app(app) # we added this so we can read & write to the users table

app.secret_key = "development-key"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
  form = SignupForm() # this is a a NEW USABLE INSTANCE OF SIGNUP FORM
  if request.method == "POST": #when the user presses submit then we take them to another page
    return "Success!"

  elif request.method == "GET": # when the user REQUESTS TO ACCESS THE SIGNUP PAGE WE RENDER THE TEMPLATE
    return render_template('signup.html', form=form)

@app.route("/shopping")
def shopping():
    food = ["Cheese","Tuna","beef"]
    return render_template("shopping.html",food=food)

if __name__ == "__main__":
    app.run()
