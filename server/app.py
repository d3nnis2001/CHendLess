from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/')
def hello():
    return "Braten ist gelanden!"

if __name__ == '__main__':
    app.run()
