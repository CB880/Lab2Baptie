import os

from flask import Flask, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

app.config ["FLASK_APP"]="app.py"

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def Home():
    return render_template("Home.html")

@app.route("/Register")
def Register():
    return render_template("Register.html")

@app.route ("/Login")
def Login():
    return render_template("Login.html")

@app.route ("/Search")
def Search():

    #Books = db.execute("SELECT isbn,title, author, year")
    #for book in Books:
    #    print(f"{title} to {author} to {year} to {isbn}")
    return render_template("Search.html")

@app.route("/find", methods=["GET", "POST"])
def find():
    query = request.form.get("query")
    print(query)
    books = db.execute('''SELECT TITLE FROM "Books" WHERE ISBN=:query''', {"query": query}).fetchall()
    return render_template("Search.html", books=books)
