import flask
from flask import request, jsonify, Blueprint
import pandas as pd
import json
# import requests
#
# # requests.get()
# # import pandas as pd
# # pd.read_json
#
# app = flask.Flask(__name__)
# app.config["DEBUG"] = True# Create some test data for our catalog in the form of a list of dictionaries.

# data = json.load('dataset.json')
# print(data)
df = pd.read_json(path_or_buf='dataset.json')
print(df)

simple = Blueprint('simple_page', __name__)


@simple.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1><p>A prototype API for distant reading of science fiction novels.</p>'''


@simple.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

@simple.route('/api/v1/resources/books', methods=['GET'])
def api_id():# Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."# Create an empty list for our results
    results = []# Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)# Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

@simple.route('/api/add_message/<uuid>', methods=['GET', 'POST'])
def add_message(uuid):
    # content = request.json
    # print(content)
    return jsonify({"uuid":uuid})


@simple.route('/api/ville/<ville>', methods=['GET'])
def ville(ville):
    return jsonify({"ville":ville})


