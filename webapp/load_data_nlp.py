from fastai.text import *


def load_language_model():
    path = 'webapp/language_model'
    path_data_lm = 'data_lm_book.pkl'
    path_learn_lm = 'mini_train_lm_book'
    data_lm = load_data(path, path_data_lm)
    learn_language_model = language_model_learner(
        data_lm, AWD_LSTM, pretrained=False).load(path_learn_lm, with_opt=False)

    return learn_language_model


def load_classification_nlp():
    path = 'webapp/class'
    path_data_class = 'data_clas'
    path_learn_class = 'mini_train_clas100_with'
    data_class = load_data(path, path_data_class)
    learn_classification_nlp = text_classifier_learner(
        data_class, AWD_LSTM, pretrained=False).load(path_learn_class, with_opt=False)

    return learn_classification_nlp
