#integration token
#content: {title,contentMarkdown,tags,coverImageURL}

import requests
import json

def postToHashnode(content,hashnodeToken):
    content['contentMarkdown']=content['content']
    if 'converImageURL' not in content.keys():
        content['coverImageURL']=''

    headers={
        'Content-Type': 'application/json',
        'Authorization': hashnodeToken,
    }
    url='https://api.hashnode.com'
    data=json.dumps(
        {
            'query':'mutation createStory($input: CreateStoryInput!){ createStory(input: $input){ code success message } }',
            'variables':{
                'input':{
                    'title':content['title'],
                    'contentMarkdown':content['contentMarkdown'],
                    'tags':{
                            '_id': '56744723958ef13879b9549b',
                            'slug': 'testing',
                            'name': 'Testing',
                            },
                    'coverImageURL':content['coverImageURL']
                }
            }
        }
    )

    response=requests.post(url,headers=headers,data=data)
    print('Hashnode Post response: ',response.content)

    return 'postToHashnode end';