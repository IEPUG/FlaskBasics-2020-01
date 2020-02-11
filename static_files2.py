from flask import Flask, Response, url_for

app = Flask(__name__)

html_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>Flask Demo</title>
    </head>
    <body>
"""

html_footer = """
    </body>
</html>
"""


@app.route('/')
def index():
    image_url = url_for('static', filename='python.png')
    html_body = """<h1>This is Python!!!</h1><img src="{0}">""".format(image_url)
    response = ''.join([html_header, html_body, html_footer])

    return Response(response, 200)


@app.route('/about')
def about():
    return Response('This is my flask app!', 200)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
