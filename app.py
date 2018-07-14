from datetime import datetime

from flask import render_template, jsonify

from custom_flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/api/tiem")
def api_time():
    return jsonify({"tiem":datetime.now().isoformat(sep=" ")})