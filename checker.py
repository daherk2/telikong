

import urllib2 as lib2

URL = 'https://stackoverflow.com/questions/'

def checker(id):
    pagina = lib2.urlopen(URL+str(id))
    conteudo = pagina.readlines()
    var = False
    for i in conteudo:
        if '<span class="vote-accepted-on load-accepted-answer-date"' in i:
            #print i
            var = True
    return var
