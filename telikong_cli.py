import requests


SERVER_ADDR = 'http://localhost'
PORT = 33336

def chck_stackoverflow(e):
    return str(requests.get(SERVER_ADDR+':'+str(PORT)+'/exception/'+str(e).replace(' ', '%20').replace("'", '').replace('"','')).text)
