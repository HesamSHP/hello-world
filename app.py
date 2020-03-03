from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/healthcheck/ok')
def check():
	ret = {"message": "EVERYTHING IS OK"}
	return jsonify(ret), 200

@app.route('/')
def main_page():
	return 'Hello World.'

def process():
	pass

if __name__ == "__main__":
	app.run('0.0.0.0',5000, debug=True)