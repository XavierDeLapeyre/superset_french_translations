#./incubator-superset/superset/translations/fr/LC_MESSAGES
import http.client
from urllib.parse import urlencode
import json
from urllib import request
import sys

key = "trnsl.1.1.20171201T151210Z.8a212d2fe07a033c.8922332ca921130acbb0662144978f3f0c97f404"

# https://translate.yandex.net/api/v1.5/tr.json/translate?key=&text=hello&lang=en-fr

messagepo  = open("messages.json", "r")
tradmessagepo = open("message2.json", "w")

myjson = json.loads(messagepo.read())

''' myjson = myjson["locale_data"]["superset"] '''

exept = 1

for row in myjson["locale_data"]["superset"]:
    if exept == 0:
        if(myjson["locale_data"]["superset"][row][0]== ''):
            urlParams = {'key': key, 'text': row, 'lang':'en-fr'}
            url = "https://translate.yandex.net/api/v1.5/tr.json/translate?" + urlencode(urlParams)
            req = request.Request(url)
            response = request.urlopen(req)

            try:
                data = response.read().decode('utf-8')
                jsonData = json.loads(data)
                if jsonData["code"] != '200':
                    print('succes')
                    myjson["locale_data"]["superset"][row][0] = [str(jsonData["text"][0])]
            except Exception as err:
                print("Unexpected error: {0}".format(err))
    else:
        exept=0

tradmessagepo.write(json.dumps(myjson, ensure_ascii=False))
