from flask import Flask, render_template, request
import urllib
import json

app = Flask(__name__)
TOKEN = '3e8cd831-519e-433c-9941-3fdc1a71868d'


@app.route('/likes', methods=['GET'])
def likes():
    token = TOKEN if request.args.get(
        'token') is None else request.args.get('token')
    url = 'https://api.gotinder.com/v2/fast-match/teasers'
    data = get_data(token, url)
    return render_template('likes.html', data=data.get('data').get('results'))


@app.route('/search', methods=['GET'])
def search():
    token = TOKEN if request.args.get(
        'token') is None else request.args.get('token')
    url = 'https://api.gotinder.com/v2/recs/core'
    data = get_data(token, url)
    return render_template('search.html', data=data.get('data').get('results'))


@app.route('/match', methods=['GET'])
def match():
    token = TOKEN if request.args.get(
        'token') is None else request.args.get('token')
    id = request.args.get('id')
    url = 'https://api.gotinder.com/like/{}'.format(id)
    get_data(token, url)
    return "NEW MATCH!!!"


def get_data(token, url):
    headers = {}
    headers['X-Auth-Token'] = token
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request).read()
    data = json.loads(response.decode("utf-8"))
    return data


if __name__ == "__main__":
    app.run(debug=True)
