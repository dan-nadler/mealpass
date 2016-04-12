import requests

PATH = 'https://api.parse.com/'

payload = {
    '_ApplicationId': "FgoCWKvEYwLPyYUEdL5vOJwCnZLhhqkNKQOSklGH",
    '_ClientVersion': "js1.6.9",
    '_InstallationId': "b99782b1-9518-db76-6b54-e67480f5a6ac",
    '_JavaScriptKey': "JvLdrSwo8sOtWUTb2kveQcVgd1YrutPG27gY8m5c",
    '_method': 'GET'
}

headers = {
    "Origin": "https://secure.mealpass.com" ,
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language": "en-US,en;q=0.8" ,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
    "Content-Type": "text/plain",
    "Accept": "*/*",
    "Referer": "https://secure.mealpass.com/login",
    "Connection": "keep-alive",
}


def login( username, password ):

    # p = payload
    p = dict()
    p['username'] = username
    p['password'] = password

    resp = requests.post(PATH+'1/login',
                         data=p )
                         # ),
                         # headers=headers)

    return  resp

if __name__ == '__main__':
    re = login( _, _ )
    print re.url
    print re.text
