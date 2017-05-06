import requests as req

problema = raw_input('Entedo com o nome do problema : \n')

urlbase = 'https://api.stackexchange.com/2.2/search/excerpts?'
parametros = 'order=desc&sort=activity&accepted=True&closed=False&site=stackoverflow&q='
problema = problema.replace(' ', '%20')  #'Date%20formatting%20not%20working%20in%20Swift%20'
url = urlbase+parametros+problema
#print url
r = req.get(url)
conteudo = r.text
print conteudo


