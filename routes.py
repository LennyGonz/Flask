from flask import Flask
from flask import render_template  #YOU HAVE TO ADD THIS TO RENDER TEMPLATES

app = Flask(__name__)
'''
@app.route('/')
@app.route('/<user>')
def users(user=None):
    return render_template("user.html",user=user)
'''

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/shopping")
def shopping():
    food = ["Cheese","Tuna","beef"]
    return render_template("shopping.html",food=food)

if __name__ == "__main__":
    app.run()
