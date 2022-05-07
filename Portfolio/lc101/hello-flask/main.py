from flask import Flask
import os 
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

template_dir = os.path.join(os.path.dirname(__file__),'templates')

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(template_dir)
)

@app.route("/")
def index():
    return "<h1>"+"Hello Flask"+"</h1>"

app.run()


