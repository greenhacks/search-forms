"""Server for the app."""
import os

os.system("source ./secrets.sh") #runs command line script in console 

from flask import (Flask, render_template, request, flash, session,
                   redirect, json, jsonify)
from jinja2 import StrictUndefined 

secretkey = os.environ['SECRET_KEY']

app = Flask(__name__)
app.secret_key = secretkey 
app.jinja_env.undefined = StrictUndefined


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')