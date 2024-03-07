import os
from flask import Flask, jsonify
from app.config import Config

# Get our configuration
def get_config():
    return Config(os.environ.get("FLASK_ENV", "dev"))

app = Flask(__name__)

# Apply our configuration to the app
app.config.from_object(get_config())

# And show what we've loaded (don't print secrets here)
print("Loading config from", get_config())
print("testing=", app.testing, "debug=",app.debug)

@app.route("/")
def index():
    return jsonify({"Hello": "World"})