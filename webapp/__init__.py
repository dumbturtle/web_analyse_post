
from flask import  Flask, render_template, request
from webapp.load_data_nlp import load_language_model, load_classification_nlp
from webapp.get_post_from_d3 import requesting_data
from webapp.save_get_db import save_class_nlp,save_lm_nlp,get_class_nlp,get_lm_nlp
from webapp.model import db

language_model = load_language_model()
classification_model = load_classification_nlp()

def create_app():
	app = Flask(__name__)
	app.config.from_pyfile('config.py')
	db.init_app(app)
	@app.route('/')
	def index():
		title = app.config['TITLE']
		return render_template('index.html', page_title=title, class_nlp_answer_db = get_class_nlp(), lm_answer_db = get_lm_nlp())
	
	@app.route('/<index>/', methods=['POST'])
	def work_with_data(index):
		title = app.config['TITLE']
		if index == 'lm_n':
			lm_text = request.form['lm_text']
			if lm_text:
				lm_text_nlp = language_model.predict(lm_text, n_words=10)
				save_lm_nlp(lm_text_nlp)
				lm_text_nlp = get_lm_nlp()
			else:
				lm_text_nlp = "Введите что-нибудь!"
			return render_template('index.html', page_title=title, lm_answer_db = lm_text_nlp, class_nlp_answer_db = get_class_nlp())
		elif index == 'class_n':
			post_url = request.form['post_url']
			if post_url:
				post_test = requesting_data(post_url)
				class_text = classification_model.predict(post_test)
				class_text = '{}'.format(class_text)
				save_class_nlp(post_url,post_test,class_text)
				class_text = get_class_nlp()
			else:
				class_text = 'Введите что-нибудь!'
			return render_template('index.html', page_title=title, lm_answer_db = get_lm_nlp(), class_nlp_answer_db = class_text)
	return app 