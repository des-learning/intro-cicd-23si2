from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hi, Dunia! Dan selamat tinggal!"


if __name__ == "__main__":
    app.run()
