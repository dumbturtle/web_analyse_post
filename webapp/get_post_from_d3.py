import requests
import re

import sys

#Запрашиваем пост с d3 по ID
def preprocess_text(text):
    text = text.lower().replace("ё", "е")
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', ' ', text)
    text = re.sub('@[^\s]+', ' ', text)
    text = re.sub('[^а-яА-Я1-9,.! ]+', ' ', text)
    text = re.sub(' +', ' ', text)
    return text.strip()

def requesting_data(post_id):
    post = re.sub('.+(\-)', '', post_id)
    post = re.sub('/.*','', post)
    post_url = "https://d3.ru/api/posts/" + str(post) + "/" 
    result_post = requests.get(post_url)
    post =  result_post.json()
    post_data = preprocess_text(post['data']['text'])
    return post_data


if __name__ == "__main__":
    text = requesting_data(int(sys.argv[1]))
    print(text)
    