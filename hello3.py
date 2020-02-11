from flask import Flask, Response

app = Flask(__name__)


@app.route('/')
def index():
    return Response('Hello World 3', 200)


@app.route('/about/')
def about():
    return Response('This is my flask app!', 200)


if __name__ == "__main__":
    app.run(debug=True,port=8080)
