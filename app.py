#$env:FLASK_ENV = "development"
#flask run

import os 
from flask import Flask

app=Flask(__name__)
app.run(debug=True)

@app.route('/')
def index():
    return 'hello world!'