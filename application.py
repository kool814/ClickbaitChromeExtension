from flask import Flask
application = Flask(__name__)
from flask import jsonify
from flask import request
import classifier

@application.route("/")
def hello():
    return "Hello World!"

@application.route('/runClassifier', methods=['POST'])
def create_title():
    if not request.json:
        abort(400)
    articleTitle = request.json['title']
    classifiedProb = classifier.classifyArticle(articleTitle)
    newsOrClickBait = ""
    if classifiedProb['clickbait'] >= 0.5:
        newsOrClickBait = 'CLICKBAIT'
    else:
        newsOrClickBait = 'NEWS'

    s = """({:.3f}% clickbait, {:.3f}% news) -> Article classified as {}\n""".format(
        classifiedProb['clickbait'] * 100, 
        classifiedProb['news'] * 100,
        newsOrClickBait)
    return s

if __name__ == "__main__":
    application.debug = True
    application.run()