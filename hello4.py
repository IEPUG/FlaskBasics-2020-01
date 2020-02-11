from flask import Flask, Response, request

app = Flask(__name__)


@app.route('/')
def index():
    arg = request.args.get('name')
    if arg is None or len(arg) == 0:
        arg = 'World'
    return Response('Hello ' + arg, 200)


@app.route('/about')
def about():
    return Response('This is my flask app!', 200)


if __name__ == "__main__":
    app.run(debug=True,port=8080)
