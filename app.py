#$env:FLASK_ENV = "development"
#flask run

import os 
import json
from flask import Flask, request

from medium import postToMedium
from hashnode import postToHashnode
from devto import postToDevto

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
        print('function postToMedium called')
        #postToMedium(content,mediumToken)
    
    hashnode=request.args.get('hashnode')
    hashnodeToken=request.args.get('hashnodeToken')
    if hashnode=='True' and hashnodeToken is not None:
        print('function postToHashnode called')
        #postToHashnode(content,hashnodeToken)

    devto=request.args.get('devto')
    devtoToken=request.args.get('devtoToken')
    if devto=='True' and devtoToken is not None:
        print('function postToDevto called')
        postToDevto(content,devtoToken)

    return 'post end'

    
    
    