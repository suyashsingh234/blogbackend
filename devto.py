#dev api key
#content : {'title','published':'true','body_markdown',tags:['discuss','help']}

import requests
import json

def postToDevto(content,devtoToken):

    if 'body_markdown' not in content.keys():
        content['body_markdown']=content['content']

    url='https://dev.to/api/articles'
    headers={
    'Content-Type': 'application/json',
    'api-key': devtoToken,
    }
    data=json.dumps(
        {
            'article': {
                    'title': content['title'],
                    'published': 'true',
                    'body_markdown': content['body_markdown'],
                    'tags': content['tags'],
            }
        }
    )

    response=requests.post(url,headers=headers,data=data)

    print('Devto Post response: ',response)

    return 'Devto end'