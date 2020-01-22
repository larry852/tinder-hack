from flask import Flask, render_template, request
import urllib
import json
from PIL import Image
import numpy as np

app = Flask(__name__)
TOKEN = '4b25cd19-cfa6-46b0-9c16-67745a6ca844'


@app.route('/likes', methods=['GET'])
def likes():
    token = TOKEN if request.args.get(
        'token') is None else request.args.get('token')
    url = 'https://api.gotinder.com/v2/fast-match/teasers'
    data = get_data(token, url)
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


@app.route('/auto-match', methods=['GET'])
def auto_match():
    count = 0
    token = TOKEN if request.args.get(
        'token') is None else request.args.get('token')
    url = 'https://api.gotinder.com/v2/fast-match/teasers'
    likes = get_data(token, url).get('data').get('results')
    url = 'https://api.gotinder.com/v2/recs/core'
    candidates = get_data(token, url).get('data').get('results')
    for like in likes:
        for candidate in candidates:
            for photo in candidate.get('user').get('photos'):
                if is_same(like.get('user').get('photos')[0].get('url'), photo.get('url')):
                    url = 'https://api.gotinder.com/like/{}'.format(
                        candidate.get('user').get('_id'))
                    get_data(token, url)
                    count += 1
                    break
    response = "{} NEW MATCHS!!!" if count > 1 else "{} NEW MATCH!!!"
    response += " Try again" if count == 0 else ""
    return response.format(count)


def get_data(token, url):
    headers = {}
    headers['X-Auth-Token'] = token
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request).read()
    data = json.loads(response.decode("utf-8"))
    return data


def exclude_profile_list(data, id):
    try:
        index = [item['user']['_id']
                 for item in data['data']['results']].index(id)
        del data['data']['results'][index]
    except:
        pass
    return data


def is_same(url1, url2):
    try:
        size = (300, 300)
        image1 = Image.open(urllib.request.urlopen(url1))
        image2 = Image.open(urllib.request.urlopen(url2))
        return list(image1.getdata()) == list(image2.getdata())
    except:
        return False


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
