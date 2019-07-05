# tinder-hack
Tool suite tinder.

## Run
```sh
git clone https://github.com/larry852/tinder-hack
cd tinder-hack
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
python app.py
```

## Endpoints
Get **token** of X-Auth-Token header on https://tinder.com, you can search by https://api.gotinder.com requests. 

### Likes service
- Get list of likes of your profile.
```sh
http://localhost:5000/likes?token=3e8cd831-519e-433c-9941-3fdc1a71868d
```

### Search service
- Get list of recomendations.
- Set age and distance range to max for get most results.
- Use click on name for give like.
```sh
http://localhost:5000/search?token=3e8cd831-519e-433c-9941-3fdc1a71868d
```

## Nice to have
- Authentication. Auto generate token.
