# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, Bukola's Cloud App!</h1><p>This is running on Flask and Azure!</p>"

if __name__ == '__main__':
    app.run(debug=True)