from flask import Flask, render_template, request
from webapp import language_model,classification_model
from webapp import app
from webapp.save_get_db import save_class_nlp, save_lm_nlp, get_class_nlp, get_lm_nlp
from webapp.get_post_from_d3 import requesting_data

@app.route('/')
def index():
	title = app.config['TITLE']
	return render_template('index.html', page_title=title, class_nlp_answer_db=get_class_nlp(), lm_answer_db=get_lm_nlp())

@app.route('/lm_n', methods=['POST'])
def work_with_lm():
    title = app.config['TITLE']
    lm_text = request.form['lm_text']
    lm_text_nlp = language_model.predict(lm_text, n_words=10)
    save_lm_nlp(lm_text_nlp)
    lm_text_nlp = get_lm_nlp()
    return render_template('index.html', page_title=title, lm_answer_db=lm_text_nlp, class_nlp_answer_db=get_class_nlp())

@app.route('/class_n', methods=['POST'])
def work_with_class():
    title = app.config['TITLE']
    post_url = request.form['post_url']
    post_test = requesting_data(post_url)
    class_text = classification_model.predict(post_test)
    class_text = '{}'.format(class_text)[10]
    save_class_nlp(post_url, post_test, class_text)
    class_text = get_class_nlp()
    return render_template('index.html', page_title=title, lm_answer_db=get_lm_nlp(), class_nlp_answer_db=class_text)