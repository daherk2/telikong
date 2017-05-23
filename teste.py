import requests

def chck_stackoverflow(e):
    return str(requests.get('http://localhost:33335/exception/'+str(e).replace(' ', '%20').replace("'", '').replace('"','')).text)

###################### Exemplo ########################
try:
    #a = 3/0
    a = a.par
    print a
except Exception as e:
    try:
        print chck_stackoverflow(e)
    except Exception as e:
        print chck_stackoverflow(e)