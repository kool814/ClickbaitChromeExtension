print ('Starting the classifier')
import classifier
print ('{}'.format("-"*80))
print ('Type \'quit\', \'q\', or \'\\q\' to exit the interactive shell')

while True:
	try:
		articleTitle = raw_input('\nArticle title: ').strip().decode('utf-8')
		if articleTitle == 'quit' or articleTitle == 'q' or articleTitle == '\q':
			break
	except:
		break
	classifiedProb = classifier.classifyArticle(articleTitle)
	newsOrClickBait = ""
	if classifiedProb['clickbait'] >= 0.5:
		newsOrClickBait = 'clickbait'
	else:
		newsOrClickBait = 'news'

	print ("""({:.3f}% clickbait, {:.3f}% news) -> Article classified as {}""".format(
		classifiedProb['clickbait'] * 100, 
		classifiedProb['news'] * 100,
		newsOrClickBait))
