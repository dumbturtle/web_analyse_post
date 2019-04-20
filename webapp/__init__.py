
from flask import Flask
from webapp.load_data_nlp import load_language_model,load_classification_nlp
from webapp.model import db

language_model = load_language_model()
classification_model = load_classification_nlp()


def create_app():
	app = Flask(__name__)
	app.config.from_pyfile('config.py')
	db.init_app(app)


	return app
	
app = create_app()	
from webapp import views