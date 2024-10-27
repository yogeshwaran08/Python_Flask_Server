from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello, World!"})

@app.route("/status")
def status():
    return jsonify({"status": "Server is running!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Host on 0.0.0.0 to make it accessible externally
