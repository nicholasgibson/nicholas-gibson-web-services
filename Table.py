import json
import urllib
import web

class Table:

    def GET(self):
        url = "http://localhost:8080/json"
        response = urllib.urlopen(url)
        jsonData = json.loads(response.read())
        render = web.template.render('templates/')
        return render.webpage(jsonData)