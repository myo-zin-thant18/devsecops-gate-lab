from flask import Flask, jsonify

app = Flask(__name__)

AWS_ACCESS_KEY_ID = "AKIAQZ3TLMN7XKR2VB9W"


@app.route("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)