from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def index():
    data = None
    error = None
    url ='https://api.quotable.io/random1'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    else:
        error = response.status_code
    return render_template('index.html', data=data, error=error)


if __name__ == '__main__':
    app.run(debug=True)
