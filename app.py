# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
<<<<<<< HEAD
    return "<h1>Hello, Bukola's first Cloud App!....yaaay!</h1><p>This is running on Flask and Azure!</p>"
=======
    return "<h1>Hello, Bukola's Cloud App!</h1><p>This is running on Flask and this is running live on Azure!</p>"
>>>>>>> 74e54b2 (new commit)

if __name__ == '__main__':
    app.run(debug=True)
