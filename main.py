


def check_stackoverflow(problema):
    import requests as req
    import json
    urlbase = 'https://api.stackexchange.com/2.2/search/excerpts?'
    parametros = 'order=desc&sort=activity&accepted=True&closed=False&site=stackoverflow&q='
    problema = problema.replace(' ', '%20')  #'Date%20formatting%20not%20working%20in%20Swift%20'
    url = urlbase+parametros+problema
    print url
    r = req.get(url)
    conteudo = str(r.text)
    conteudo = json.loads(conteudo)
    for i in range(0,len(conteudo['items'])):
        if conteudo['items'][i]['is_accepted'] == 'true':
            tags = conteudo['items'][i]['tags']
            tagp = ''
            for tag in tags:
                tagp = tagp + " " + tag
            print tagp
            bodies = conteudo['items'][i]['body']
            print bodies




