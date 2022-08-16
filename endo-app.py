from crypt import methods
from flask import Flask
from flask import request
from git import Repo
from urllib.request import urlopen
import re
import json
import urllib
import logging


app = Flask(__name__)


# helloworld endpoint
@app.route("/helloworld")   

def hello_world():
    
    name = request.args.get("name")  
    
    if name is None:
        return "Hello Stranger"
    else:    
        cut_case = re.sub(r"(?<!^)(?=[A-Z])", " ", name)
        return str(cut_case)

# versionz endpoint
@app.route("/versionz")

def get_git_stuff():
    
    url = "https://api.github.com/repos/matija-knezevic/endocode-challenge/commits"
    
    request = urllib.request.Request(
        url,
        data=None,
        headers={
            "User-Agent": "endocode-challenge by github.com/matija-knezevic/endocode-challenge"
        }
    )
    response = urllib.request.urlopen(request)
    return json.loads(response.read().decode("utf-8")) 

# Logging
logging.basicConfig(
        filename="endo-app.log",
        format="%(asctime)s %(levelname)-8s %(message)s",
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S")