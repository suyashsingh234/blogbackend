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
    
    ###########post parse
    formData=request.form
    formData=formData.to_dict()
    formData=list(formData.keys())[0]
    formData=json.loads(formData)
    ###########

    #################variables 
    content=medium=mediumToken=hashnode=hashnodeToken=devto=devtoToken=None

    if 'content' in formData.keys():
        content= formData['content']
        content=json.loads(content)
    if 'medium' in formData.keys():
        medium=formData['medium']
    if 'mediumToken' in formData.keys():
        mediumToken=formData['mediumToken']
    if 'hashnode' in formData.keys():
        hashnode=formData['hashnode']
    if 'hashnodeToken' in formData.keys():
        hashnodeToken=formData['hashnodeToken']
    if 'devto' in formData.keys():
        devto=formData['devto']
    if 'devtoToken' in formData.keys():
        devtoToken=formData['devtoToken']
    ####################################

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

    print(response)
    return json.dumps(response)

    
    
if __name__=='__main__':
    app.run(debug=True,port=PORT)