from flask import Flask

app = Flask(__name__)

@app.route("/")
def get_news():
	return "no news is good news"
if __name__ == '__main__':
	app.run(host="192.168.137.10", port=5000, debug=True)
