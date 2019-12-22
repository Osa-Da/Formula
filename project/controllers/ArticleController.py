from flask import jsonify
from project import db
from project.database.model.Article import Article

class ArticleController():
    def new(self, request):
        """ Create new Article model and return it
        :param request: flask.Request"""
        jsonRequest = request.get_json(force=True)
        for articleObject in jsonRequest:
            newArticle = Article(
                articleObject['title'], articleObject['description'],
                articleObject['text'], articleObject['data'],
                articleObject['photo'], getRegion(jsonRequest)
                # self.getRegion(articleObject)
            )
            db.session.add(newArticle)
            db.session.commit()

        return jsonify({
            'error': False,
            'error_message': ''
        })

    def getParams(self, request):
        return {
            'offset' : request.args.get('offset'),
            'limit' : request.args.get('limit'),
            'region' : request.args.get('region')
        }

    def getRegion(self, dict):
        return dict['region'] if 'region' in dict.keys() else 0

    def getOffset(self, dict):
        return dict['offset'] if 'offset' in dict.keys() else 0

    def getLimit(self, dict):
        return dict['limit'] if 'limit' in dict.keys() else 1

    def get(self, request):
        jsonRequest = {}
        if (request.is_json == True):
            jsonRequest = request.get_json(force=True)
        else:
            jsonRequest = self.getParams(request)

        articles = self.getArticles(
            self.getOffset(jsonRequest), self.getLimit(jsonRequest),
            self.getRegion(jsonRequest)
        )

        articlesJson = []
        for article in articles:
            articlesJson.append({
                'title': article.title, 'description': article.description,
                'text': article.text, 'date': article.date.strftime("%m/%d/%Y"),
                'images': article.images, 'region': article.region,
                'id':article.id
            })

        return jsonify(articlesJson)

    def getArticles(self, offset, limit, region = 0):
        if int(region) > 0:
            return Article.query.order_by(Article.date.desc())\
                .filter(Article.region == region)\
                .offset(int(offset))\
                .limit(int(limit))\
                .all()
        else:
            return Article.query.order_by(Article.date.desc())\
                .offset(int(offset))\
                .limit(int(limit))\
                .all()
