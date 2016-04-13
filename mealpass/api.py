import requests
import httplib, urllib
import json

class mealpass(object):

    def __init__(self, username, password):
        self.PATH = 'https://api.parse.com/'

        self.payload = {
            '_ApplicationId': "FgoCWKvEYwLPyYUEdL5vOJwCnZLhhqkNKQOSklGH",
            '_ClientVersion': "js1.6.9",
            '_InstallationId': "b99782b1-9518-db76-6b54-e67480f5a6ac",
            '_JavaScriptKey': "JvLdrSwo8sOtWUTb2kveQcVgd1YrutPG27gY8m5c",
            '_method': 'GET',
            'username': username,
            'password': password
        }

        self.headers = {
            "Origin": "https://secure.mealpass.com" ,
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language": "en-US,en;q=0.8" ,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
            "Content-Type": "text/plain",
            "Accept": "*/*",
            "Referer": "https://secure.mealpass.com/login",
            "Connection": "keep-alive",
        }


    def login(self):

        resp = requests.post(self.PATH+'1/login',
                             data=json.dumps(self.payload),
                             headers=self.headers)

        self.login_resp = json.loads(resp.text)
        del self.payload['username']
        del self.payload['password']
        del self.payload['_method']
        self.payload['sessionToken'] = str(self.login_resp[u'sessionToken'])
        return json.loads(resp.text)

    def search(self):

        p = {"search":
                {
                    "onlyFavorites": False,
                    "text": "",
                    "cities": ["N9H3AGq93v", "N9H3AGq93v"],
                    "cuisines": ["american", "asian", "latin", "mediterranean", "italian"],
                    "portions": [1, 2, 3],
                    "neighborhoods": [],
                    "timezone": -4,
                    "limit": 10,
                    "skip": 0
                },
            "_ApplicationId": "FgoCWKvEYwLPyYUEdL5vOJwCnZLhhqkNKQOSklGH",
            "_JavaScriptKey": "JvLdrSwo8sOtWUTb2kveQcVgd1YrutPG27gY8m5c",
            "_ClientVersion": "js1.6.9",
            "_InstallationId": "db165b9c-414e-7cb8-f907-0d5123515678",
            "_SessionToken": self.payload['sessionToken']
        }

        resp = requests.post(self.PATH+'1/functions/searchMeal',
                             data=json.dumps(p),
                             headers=self.headers)

        self.search_resp = json.loads(resp.text)
        return json.loads(resp.text)

    def reserve(self, restaurant_name=u'Tossed'):

        p = self.payload
        p['pickupTime'] =  "12:00pm-12:15pm"

        data = [
            {
                'meal': str(r['meal']['objectId']),
                'restaurant': str(r['restaurant']['objectId']),
                'city': str(r['restaurant']['city']['objectId']),
                'schedule': str(r['objectId'])
            }
            for r in re['result'] if r['restaurant']['name'] == restaurant_name
        ][0]

        for k, v in data.iteritems():
            p[k] = v

        print json.dumps(p)

        #TODO fix error from this request
        resp = requests.post(self.PATH+'1/functions/reserveMeal',
                             data=json.dumps(p),
                             headers=self.headers)

        print resp.text
        self.reservation_resp = json.loads(resp.text)
        self.reservation_id = self.reservation_resp['objectId']

        return json.loads(resp.text)

    def cancel(self):

        p = self.payload
        del p['_method']

        p['reservation'] = self.reservation_idr
        p['city'] = self.reservation_id['user']['city']['objectId']

        resp = requests.post(self.PATH + '1/functions/cancelReservation',
                             data=json.dumps(p),
                             headers=self.headers)

        return json.loads(resp.text)


if __name__ == '__main__':
    m = mealpass( 'mylogin','mypassword')
    re = m.login()
    re = m.search()

    print 'reserving tossed'
    re = m.reserve(restaurant_name=u'Tossed')
    print re

    print 'cancelling tossed'
    re = m.cancel()
    print re