from crypt import methods
from flask import Flask
from flask import request
import re

app = Flask(__name__)

# First endpoint
@app.route("/helloworld")   

def hello_world():
    
    name = request.args.get("name")  
    
    if name is None:
        return "Hello Stranger"
    else:    
        cut_case = re.sub(r'(?<!^)(?=[A-Z])', ' ', name)
        return str(cut_case)