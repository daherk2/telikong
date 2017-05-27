from flask import Flask
import app
import re
import rethinkdb as r
import json

apps = Flask(__name__)

@apps.route('/exception/<excep>')
def main(excep):
    model = '''
    {
    	"links": xxxxx
    }
    '''
    var = app.check_stackoverflow(excep)
    conn = r.connect('localhost', 32901).repl()
    links = var.split(',')
    texto = ''
    model = str(model).replace('xxxxx', str(links[1:]))
    model = model.replace("'", '"')
    #print model
    r.db('Telikong').table('Exceptions').insert(json.loads(model)).run()
    return var


if __name__ == '__main__':
  apps.run(port=33336)