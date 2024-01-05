# KnightSolutions Canada
# www.KnightSolutions.ca - Secured and Responsive Web Technologies
# Aug 22,2023

from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')

# Start - Local functions not in route
user = "mark"
password = "warfreaker"

# End - Local functions not in route


# Start - Route functions
# Index Page (Landing)
@app.route("/", methods=['POST', 'GET'])
@app.route("/index", methods=['POST', 'GET'])
def landing():
    return render_template("index.html")


@app.route("/doc", methods=['POST', 'GET'])
@app.route("/documentation", methods=['POST', 'GET'])
def docs():
    return render_template("doc.html")


# End - Route functions


app.secret_key = '\xb2\xcb\x06\x85\xb1\xcfZ\x9a\xcf\xb3h\x13\xf6\xa6\xda)\x7f\xdd\xdb\xb2BK>'
