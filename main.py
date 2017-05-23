


def check_stackoverflow(problema):
    import requests as req
    import json
    urlbase = 'https://api.stackexchange.com/2.2/search/excerpts?'
    parametros = 'order=desc&sort=activity&accepted=True&closed=False&site=stackoverflow&q='
    problema = str(problema).replace(' ', '%20')  #'Date%20formatting%20not%20working%20in%20Swift%20'
    url = urlbase+parametros+problema
    print url
    r = req.get(url)
    conteudo = u' '.join((r.text, '')).encode('utf-8').strip()
    conteudo = json.loads(conteudo)
    for i in range(0,len(conteudo['items'])):
        tags = conteudo['items'][i]['tags']
        tagp = ''
        for tag in tags:
            tagp = tagp + " " + tag
        print tagp
        bodies = conteudo['items'][i]['body']
        print bodies
        idq = conteudo['items'][i]['question_id']
        base_answers = 'https://api.stackexchange.com/2.2/questions/'+str(idq)+'/answers?order=desc&sort=activity&site=stackoverflow'
        print base_answers
        r = req.get(base_answers)
        cont_answer = u' '.join((r.text, '')).encode('utf-8').strip()
        data_answer = json.loads(cont_answer)
        for i in range(0,len(data_answer['items'])):
            print data_answer['items'][i]

###################### Exemplo ########################
try:
    a = 3/0
    print a
except Exception as e:
    try:
        check_stackoverflow(e)
    except Exception as e:
        check_stackoverflow(e)

