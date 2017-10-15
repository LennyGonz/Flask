from flask import Flask
from flask import render_template  #YOU HAVE TO ADD THIS TO RENDER TEMPLATES

app = Flask(__name__)

@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html", name=name) # we need to insert the name of the html file
                                                      # we also need to include our name variable
if __name__ == "__main__":
    app.run()
