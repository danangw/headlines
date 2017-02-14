import feedparser
from flask import Flask
from flask import render_template

app = Flask(__name__)

rss_feed = {    'detik': 'http://rss.detik.com/index.php/detikcom',
		'viva': 'http://rss.viva.co.id/get/politik',
		'antara': 'http://www.antaranews.com/rss/art.xml',
		'liputan6': 'http://feed.liputan6.com/actual' }	

@app.route("/")
@app.route("/detik")
def detik():
	return get_news('detik')
@app.route("/viva")
def viva():
	return get_news('viva')
@app.route("/antara")
def antara():
	return get_news('antara')
@app.route("/liputan6")
def liputan6():
	return get_news('liputan6')

def get_news(publication):
	feed = feedparser.parse(rss_feed[publication])
	#first_article = feed['entries'][0]
	return render_template("home3.html", articles=feed['entries'])
	#	title=first_article.get("title"),
	#	published=first_article.get("published"),
	#	summary=first_article.get("summary"))	
        
if __name__ == '__main__':
	app.run(host="192.168.137.10", port=5000, debug=True)
