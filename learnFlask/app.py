from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello user! This is my first Flask app."

@app.route("/about")
def about():
    return "This is the about page of my first Flask app."

@app.route("/contact")
def contact():
    return "This is the contact page of my first Flask app."

if __name__ == "__main__":
    app.run(debug=True)

