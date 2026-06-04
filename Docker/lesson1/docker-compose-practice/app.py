from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        database=os.environ.get("DB_NAME", "appdb"),
        user=os.environ.get("DB_USER", "sandip"),
        password=os.environ.get("DB_PASS", "secret123")
    )

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/db-check")
def db_check():
    try:
        conn = get_db()
        conn.close()
        return jsonify({"database": "connected"})
    except Exception as e:
        return jsonify({"database": "failed", "error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)