from flask import Flask
from models import db

votr = Flask(__name__)

#load config form teh config file we created earlier
votr.config.from_object('config')

#initialize and create the database
db.init_app(votr)
db.create_all(app=votr)

@votr.route('/')
def home():
    return 'hello world'

@votr.route('/it')
def run_home():
    return 'wudup homie'

if __name__ == '__main__':
    votr.run()
