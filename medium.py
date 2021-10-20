# integration token
# content={"title": "Liverpool FC",
#  "contentFormat": "html",
#  "tags": ["football", "sport", "Liverpool"]
#   }
# mediumToken = <integration token>

import requests
import json
import ast

#a={'hello':'world','suyash':'singh'}
#print(a['hello'])

def getAuthorId(mediumToken):
    headers={
        'Host': 'api.medium.com',
        'Authorization': 'Bearer '+mediumToken,
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Accept-Charset': 'utf-8'
        }
    url='https://api.medium.com/v1/me'

    response=requests.get(url,headers=headers)
    response=response.content
    response=json.loads(response)


    return response['data']['id']

def postToMedium(content,mediumToken):
    authorId=getAuthorId(mediumToken)

    content['tags']=ast.literal_eval(content['tags'])
    print(content['tags'])

    url='https://api.medium.com/v1/users/'+authorId+'/posts'
    headers={
            'Host': 'api.medium.com',
            'Authorization': 'Bearer '+mediumToken,
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Accept-Charset': 'utf-8'
            }
    data=json.dumps(
        {
        'title':content['title'],
        'contentFormat':'html',
        'content':content['content'],
        'tags':content['tags']
        }
    )

    #print(url,headers,data)
    #print(data)
    
    response=requests.post(url,headers=headers,data=data)

    #print(response.content)

    return response.status_code
