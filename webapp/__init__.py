
from flask import  Flask, render_template, request

def create_app():
	app = Flask(__name__)
	app.config.from_pyfile('config.py')
	@app.route('/')
	def index():
		title = app.config['TITLE']
		lm_text = 'Здесь будет ответ языковой модели'
		class_text = 'Здесь будет ответ нейросети'
		return render_template('index.html', page_title=title, class_answer=class_text, lm_answer=lm_text)
	
	@app.route('/<index>/', methods=['POST'])
	def work_with_data(index):
		title = app.config['TITLE']
		lm_text = 'Здесь будет ответ языковой модели'
		class_text = 'Здесь будет ответ нейросети'
		if index == 'lm_n':
			lm_text = request.form['lm_text']
			#return render_template('index.html', page_title=title, lm_answer=lm_text, class_answer=class_text)
		elif index == 'class_n':
			class_text = request.form['class_text']
		
		return render_template('index.html', page_title=title, class_answer=class_text, lm_answer=lm_text)
	return app 