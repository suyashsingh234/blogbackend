# integration token
# content={"title": "Liverpool FC",
#  "contentFormat": "html",
#  "content": "<h1>Liverpool FC</h1><p>You’ll never walk alone.</p>",
#  "tags": ["football", "sport", "Liverpool"]
#   }
# mediumToken = <integration token>

import requests
import json

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
        'contentFormat':content['contentFormat'],
        'content':content['content'],
        'tags':content['tags']
    }
    )
    
    response=requests.post(url,headers=headers,data=data)
    print('Medium Post response: ',response)

    return 'postToMedium end'
