from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    name = "sharique"
    return render_template('index.html', name=name)


@app.route('/sharique/')
def sharique():
    return 'Hello sharique bhai!'


if __name__ == "__main__":
    app.debug = True
    app.run()

class 