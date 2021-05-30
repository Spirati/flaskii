# FLASKII - the world's worst ASCII converter ever

## Setting up locally
Clone the repository, create the environment (`conda env create -f environment.yml`), and create a file called `.env` using this template:
```
FLASK_KEY=
```
Put whatever random gibberish (or even an actual secret key) you'd like after the `=`; this will serve to secure the user session. You can serve it using either `flask run` for development or `gunicorn` for production, both are provided in the environment!