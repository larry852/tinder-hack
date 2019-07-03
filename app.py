from flask import Flask, render_template, request
import urllib
import json

app = Flask(__name__)
TOKEN = '3e8cd831-519e-433c-9941-3fdc1a71868d'


@app.route('/', methods=['GET'])
def index():
    token = TOKEN if request.args.get(
        'token') is None else request.args.get('token')
    data = get_data(token)
    return render_template('index.html', data=data.get('data').get('results'))


def get_data(token):
    url = 'https://api.gotinder.com/v2/fast-match/teasers'
    headers = {}
    headers['X-Auth-Token'] = token
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request).read()
    data = json.loads(response.decode("utf-8"))
    return data


if __name__ == "__main__":
    app.run(debug=True)
