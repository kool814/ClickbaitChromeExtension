from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route('/test', methods=['POST'])
def test():
    if request.method == 'POST':
        classifiedProb = classifier.classifyArticle(articleTitle)
        newsOrClickBait = ""
        if classifiedProb['clickbait'] >= 0.5:
            newsOrClickBait = '**CLICKBAIT**'
        else:
            newsOrClickBait = 'NEWS'

        s = """({:.3f}% clickbait, {:.3f}% news) -> Article classified as {}""".format(
            classifiedProb['clickbait'] * 100, 
            classifiedProb['news'] * 100,
            newsOrClickBait)
        return s
        # return do_the_login()
    else:
        return show_the_login_form()

# @application.route("/test")
# def test():
#     return "Test"

if __name__ == "__main__":
    application.run()