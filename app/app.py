from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route('/check')
def check():
    ret = {"message": "EVERYTHING IS OK"}
    return jsonify(ret), 200


@app.route('/')
def main_page():
    passed_data = {'author_name': 'Hesam'}
    return render_template('index.html', data=passed_data)


def process():
    pass


if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)
