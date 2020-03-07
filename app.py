from flask import Flask
app = Flask(__name__)


@app.route('/')
def main_page():	
	return 'Hello World'

@app.route('/check')
def check_app():
	return 'Everything is OK.'

if __name__== '__main__':
	app.run('0.0.0.0',5000, True)




