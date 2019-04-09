import glob
import json
import numpy
import sys
import nltk
from itertools import imap
from operator import itemgetter
from random import shuffle
from sklearn import metrics
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


def classifyArticle(title):
  predictions = nb_classifier.predict_proba(vectorizer.transform(numpy.array([title_cleaner(title)])))[0]
  probabilities = dict(zip(nb_classifier.classes_, predictions))
  return probabilities

def title_cleaner(title):
    return title

# def show_most_informative_features(vectorizer, clf, n):
#     feature_names = vectorizer.get_feature_names()
#     coefs_with_fns = sorted(zip(clf.coef_[0], feature_names))
#     top = zip(coefs_with_fns[:n], coefs_with_fns[:-(n + 1):-1])
#     for (coef_1, fn_1), (coef_2, fn_2) in top:
#         print "\t%.4f\t%-15s\t\t%.4f\t%-15s" % (coef_1, fn_1, coef_2, fn_2)

def category_cleaner(category):
  return 'clickbait' if category else 'news'

training_proportion = 0.8
training_data = []
testing_data = []
data = glob.glob('./data/*.json')

for filename in data:
  with open(filename, 'rb') as inFile:
    dataset = json.load(inFile)
    cutoff = int(round(len(dataset) * training_proportion))
    training_data.extend(dataset[0:cutoff])
    testing_data.extend(dataset[cutoff:])
    # print 'Loaded %d headlines from %s' % (len(dataset), filename)

article_titles = map(itemgetter('article_title'), training_data)
clickbait_values = map(category_cleaner, imap(itemgetter('clickbait'), training_data))
test_article_titles = map(itemgetter('article_title'), testing_data)
test_clickbait_values = map(category_cleaner, imap(itemgetter('clickbait'), testing_data))

X_train = numpy.array(article_titles)
Y_train = numpy.array(clickbait_values)
X_test = numpy.array(test_article_titles)
Y_test = numpy.array(test_clickbait_values)

vectorizer = TfidfVectorizer(ngram_range=(1, 3), lowercase=True, stop_words='english', strip_accents='unicode', min_df=2, norm='l2')

X_train = vectorizer.fit_transform(X_train)
nb_classifier = MultinomialNB()
nb_classifier.fit(X_train, Y_train)

X_test = vectorizer.transform(X_test)
Y_predicted = nb_classifier.predict(X_test)

print 'sklearn report:'
print metrics.classification_report(Y_test, Y_predicted)

# show_most_informative_features(vectorizer, nb_classifier, 20)
