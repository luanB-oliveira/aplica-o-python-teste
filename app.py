from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Olá mundo! Deploy teste na Koyeb com Python e Flask"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)