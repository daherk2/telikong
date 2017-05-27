
import requests as req
import json
import checker as chk


def check_stackoverflow(problema):
    urlbase = 'https://api.stackexchange.com/2.2/search/excerpts?'
    parametros = 'order=desc&sort=activity&accepted=True&closed=False&site=stackoverflow&q='
    problema = str(problema).replace(' ', '%20')  #'Date%20formatting%20not%20working%20in%20Swift%20'
    url = urlbase+parametros+problema
    #print url
    r = req.get(url)
    conteudo = u' '.join((r.text, '')).encode('utf-8').strip()
    conteudo = json.loads(conteudo)
    saida = ''
    print "Numero de queries encontradas : "+str(len(conteudo['items']))
    for i in range(0,len(conteudo['items'])):
        tags = conteudo['items'][i]['tags']
        tagp = ''
        for tag in tags:
            tagp = tagp + " " + tag
        bodies = conteudo['items'][i]['body']
        idq = conteudo['items'][i]['question_id']
        base_answers = 'https://api.stackexchange.com/2.2/questions/'+str(idq)+'/answers?order=desc&sort=activity&site=stackoverflow'
        r = req.get(base_answers)
        cont_answer = u' '.join((r.text, '')).encode('utf-8').strip()
        data_answer = json.loads(cont_answer)
        try:
            if chk.checker(idq):
                saida = saida + ' , https://stackoverflow.com/questions/' + str(idq)
        except:
            pass
    return saida

