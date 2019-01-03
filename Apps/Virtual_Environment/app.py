from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/')
def index():
    return "hello"

if __name__ == "__main__":
    app.run(debug=True)