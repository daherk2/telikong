from flask import Flask
import app
import re

apps = Flask(__name__)

@apps.route('/exception/<excep>')
def main(excep):
    return app.check_stackoverflow(excep)


if __name__ == '__main__':
  apps.run(port=33336)