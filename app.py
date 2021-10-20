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
    content=request.get_data()
    content=json.loads(content)

    response=dict()

    medium=request.args.get('medium')
    mediumToken=request.args.get('mediumToken')
    if medium=='True' and mediumToken is not None:
        print('function postToMedium called')
        response['Medium']=postToMedium(content,mediumToken)
    
    hashnode=request.args.get('hashnode')
    hashnodeToken=request.args.get('hashnodeToken')
    if hashnode=='True' and hashnodeToken is not None:
        print('function postToHashnode called')
        response['Hashnode']=postToHashnode(content,hashnodeToken)

    devto=request.args.get('devto')
    devtoToken=request.args.get('devtoToken')
    if devto=='True' and devtoToken is not None:
        print('function postToDevto called')
        response['Devto']=postToDevto(content,devtoToken)

    return json.dumps(response)

    
    
if __name__=='__main__':
    app.run(debug=True,port=PORT)