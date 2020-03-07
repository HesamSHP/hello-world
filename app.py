from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/healthcheck/ok')
def check():
	ret = {"message": "EVERYTHING IS OK"}
	return jsonify(ret), 200

@app.route('/')
<<<<<<< HEAD
def main_page():	
	return 'Hello World'

@app.route('/check')
def check_app():
	return 'Everything is OK.'

if __name__== '__main__':
	app.run('0.0.0.0',5000, True)




=======
def main_page():
	return 'Hello World.'

def process():
	pass

if __name__ == "__main__":
	app.run('0.0.0.0',5000, debug=True)
>>>>>>> d9a8328d2bb4ef2bfbc8b744b313381a9dff8577
