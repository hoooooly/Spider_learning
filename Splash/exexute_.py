import requests
import json

lua_scrpit = '''
    function main(splash)
        splash:go("http://example.com")
        splash: wait(0.5)
        local title=splash:evaljs("document.title")
        return{title=title)
    end
'''

splash_url = 'http://localhost:8050/execute'
headers = {'content-type': 'application/json'}
data = json.dumps({'lua_source': lua_scrpit})
response = requests.post(splash_url, headers=headers, data=data)
response.content

response.json()
