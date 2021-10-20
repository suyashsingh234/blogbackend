#$env:FLASK_ENV = "development"
#flask run

import os 
import json
from flask import Flask, request
from flask_cors import CORS, cross_origin

from medium import postToMedium
from hashnode import postToHashnode
from devto import postToDevto

PORT = os.environ.get('PORT',5000)

app=Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def index():
    return 'hello world!'

@app.route('/post',methods=['POST'])
@cross_origin()
def post():
    content=request.form.get('content')
    medium=request.form.get('medium')
    mediumToken=request.form.get('mediumToken')
    hashnode=request.form.get('hashnode')
    hashnodeToken=request.form.get('hashnodeToken')
    devto=request.form.get('devto')
    devtoToken=request.form.get('devtoToken')

    print(content,devtoToken)

    content=json.loads(content)

    response=dict()

    
    if medium=='True' and mediumToken is not None:
        print('function postToMedium called')
        response['Medium']=postToMedium(content,mediumToken)
    
    if hashnode=='True' and hashnodeToken is not None:
        print('function postToHashnode called')
        response['Hashnode']=postToHashnode(content,hashnodeToken)

    if devto=='True' and devtoToken is not None:
        print('function postToDevto called')
        response['Devto']=postToDevto(content,devtoToken)

    return json.dumps(response)

    
    
if __name__=='__main__':
    app.run(debug=True,port=PORT)