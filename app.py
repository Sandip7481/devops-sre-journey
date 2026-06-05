from flask import Flask, jsonify
import psycopg2
import requests
import os

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "version": "2.0",
        "builder": "multi-stage"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)