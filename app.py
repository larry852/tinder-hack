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
    remove_profile(data, '81bb473a-d11c-46f1-8825-a4b49c88ba34')
    return render_template('likes.html', data=data.get('data').get('results'), token=token)


@app.route('/search', methods=['GET'])
def search():
    token = TOKEN if request.args.get(
        'token') is None else request.args.get('token')
    url = 'https://api.gotinder.com/v2/recs/core'
    data = get_data(token, url)
    return render_template('search.html', data=data.get('data').get('results'), token=token)


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


def remove_profile(data, id):
    try:
        index = [item['user']['_id']
                 for item in data['data']['results']].index(id)
        del data['data']['results'][index]
    except:
        pass
    return data


if __name__ == "__main__":
    app.run(debug=True)
