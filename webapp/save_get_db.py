from webapp.model import db, lm_nlp, class_nlp
import webapp.config 

def save_lm_nlp(text):
    lm_text_db = lm_nlp(text=text)
    db.session.add(lm_text_db)
    db.session.commit()

def save_class_nlp(url,text,rating):
    class_nlp_db = class_nlp(url=url, text=text, rating=rating)
    db.session.add(class_nlp_db)
    db.session.commit()

def get_lm_nlp():
    lm_text = lm_nlp.query.order_by(lm_nlp.id.desc()).limit(webapp.config.LIMIT_COUNT)
    return lm_text

def get_class_nlp():
    class_nlp_text = class_nlp.query.order_by(class_nlp.id.desc()).limit(webapp.config.LIMIT_COUNT)
    return class_nlp_text 