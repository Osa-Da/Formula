import requests
import json
from project.config import HOST
from project import app
from project.controllers import articleController
from project import getHost
from project.config import HOST
from flask import request, render_template
from project import db
from project.database.model.Article import Article


@app.route('/db')
def db():
    with open('C:\\Users\\oxybe\\Desktop\\База\\NaAvtotrase.json', "r", encoding="utf-8") as file:
        basa = json.load(file)
        for ad in basa:
            
            article = Article(ad['title'], ad['description'], ad['text'], ad['data'], ad['photo'], 0)
            db.session.add(article)
            db.session.commit()
            





@app.route('/')
def index():
    data = {
        "offset" : 0,
        "limit" : 20,
        "region" : 0
    }
    ads = requests.post(getHost('/api/article/get'), json=data)
    answer = json.loads(ads.text)
    return render_template('news.html', ads=answer)

@app.route('/city')
def city():
    data = {
        "offset" : 0,
        "limit" : 20,
        "region" : 72
    }
    ads = requests.post(getHost('/api/article/get'), json=data)
    answer = json.loads(ads.text)
    return render_template('city.html', ads=answer)

@app.route('/justice')
def justice():
    return render_template('justice.html')

@app.route('/ideas')
def ideas():
    return render_template('ideas.html')

@app.route('/news')
def news():
    data = {
        "offset" : 0,
        "limit" : 20,
        "region" : 0
    }
    ads = requests.post(getHost('/api/article/get'), json=data)
    answer = json.loads(ads.text)
    return render_template('news.html', ads=answer)


@app.route('/maps')
def maps():
    return render_template('maps.html')

@app.route('/api/article/new', methods=['POST'])
def article_new():
    return articleController.new(request)

@app.route('/api/article/get', methods=['POST', 'GET'])
def article_get():
    return articleController.get(request)
