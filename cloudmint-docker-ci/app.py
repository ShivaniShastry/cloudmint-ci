from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "CloudMint Flask Service CI/CD Test is Running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=12032)
