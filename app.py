# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, This is Bukola's first Cloud App!...Yaaay!</h1><p>This is running on Flask and Azure!</p>"

if __name__ == '__main__':
    app.run(debug=True)
