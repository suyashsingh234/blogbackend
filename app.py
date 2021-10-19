#$env:FLASK_ENV = "development"
#flask run

import os 
import json
from flask import Flask, request

from medium import postToMedium

app=Flask(__name__)
app.run(debug=True)

@app.route('/')
def index():
    return 'hello world!'

@app.route('/post',methods=['POST'])
def post():
    content=request.get_data()
    content=json.loads(content)

    medium=request.args.get('medium')
    mediumToken=request.args.get('mediumToken')
    if medium=='True' and mediumToken is not None:
        postToMedium(content,mediumToken)
    return 'post end'

    
    
    