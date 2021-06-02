from flask import Flask

app1 = Flask(__name__)
app2 = Flask(__name__)

@app1.route('/')
def index():
    return "app1!"

if __name__ == "__main__":
    app1.run(port=5001)


@app2.route('/')
def index():
    return "app2!"

if __name__ == "__main__":
    app2.run(port=5002)