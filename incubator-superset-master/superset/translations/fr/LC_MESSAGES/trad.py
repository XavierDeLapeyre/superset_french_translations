#./incubator-superset/superset/translations/fr/LC_MESSAGES
import http.client
from urllib.parse import urlencode
import json
from urllib import request
import sys

key = "trnsl.1.1.20171201T151210Z.8a212d2fe07a033c.8922332ca921130acbb0662144978f3f0c97f404"

# https://translate.yandex.net/api/v1.5/tr.json/translate?key=&text=hello&lang=en-fr

messagepo  = open("messages.po", "r")
tradmessagepo = open("message2.po", "w")

line = messagepo.readline()

while line != None:
    if "msgid" not in line:
        tradmessagepo.write(line)
    else:
        tradmessagepo.write(line)
        inStr = line.split("\"")[1]

        if(inStr != ''):
            #print("inStr" + inStr)
            line = messagepo.readline()
            outStr = line.split("\"")[1]

            if(outStr == ''):

                urlParams = {'key': key, 'text': inStr, 'lang':'en-fr'}
                url = "https://translate.yandex.net/api/v1.5/tr.json/translate?" + urlencode(urlParams)
                req = request.Request(url)
                response = request.urlopen(req)

                try:
                    data = response.read().decode('utf-8')
                    jsonData = json.loads(data)
                    if jsonData["code"] != '200':
                        outStr = str(jsonData["text"][0])
                    else:
                        outStr = ''

                except Exception as err:
                    print("Unexpected error: {0}".format(err))

            tradmessagepo.write("msgstr \""+outStr+"\"\n")
            print(outStr)
 
    line = messagepo.readline()
