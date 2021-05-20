from flask import Blueprint, jsonify, request, Response, render_template
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

# with open('dataset.json') as json_file:
#     data = json.load(json_file)
# print(type(data))
# df = pd.read_json(path_or_buf='dataset.json')
# print(df)

API = Blueprint('simple_page', __name__)


@API.route('/API/v1/list_all', methods=['GET'])
def get_all():
    """
    Function that returns all investments in JSON format.
    :return: json with all investments
    """
    with open('dataset.json') as json_file:
        data = json.load(json_file)
    return jsonify(data)


# List investments filtered by ville and/or by etat_d_avancement

@API.route('/API/v1/list', methods=['GET'])
def get_from_base():
    """
    Function that allows to filter by ville and/or etat_d_avancement
    To filter, use the ville and etat_d_avancement as URL parameters
    :return: json that contains the filtered data
    """
    args = request.args
    data = pd.read_json("dataset.json")
    if 'ville' in args:
        data = data.drop(data[data['ville'] != args['ville']].index)

    if 'etat_d_avancement' in args:
        data = data.drop(data[data['etat_d_avancement'] != args['etat_d_avancement']].index)

    data = data.dropna(axis=1)

    if data.shape[0] < 1:
        return Response("Combnation not found", status=404)
    return jsonify(data.to_dict('records'))


# List investments by id

@API.route('/API/v1/list/by_id/<id>', methods=['GET'])
def get_by_id(id):
    """
    Function that allows to filter by id
    :return: json that contains the filtered data
    """
    data = pd.read_json("dataset.json")
    # data = data.drop(data[data['codeuai'] != id].index)
    # data = data.dropna(axis=1)
    try:
        data = data.iloc[int(id)]
        data = data.dropna()
    except:
        return Response("Invalid id", status=404)
    return jsonify(data.to_dict())


# List investments by id

@API.route('/single_view/<id>', methods=['GET'])
def view_by_id(id):
    """
    Function that creates a view for a single investment
    """
    data = pd.read_json("dataset.json")
    try:
        data = data.iloc[int(id)]
        data = data.dropna()
    except:
        return Response("Invalid id", status=404)

    data = data.to_dict()
    return render_template("single_view.html", data=data)

# @simple.route('/', methods=['GET'])
# def home():
#     return '''<h1>Distant Reading Archive</h1><p>A prototype API for distant reading of science fiction novels.</p>'''
#
#
# @simple.route('/api/v1/resources/books/all', methods=['GET'])
# def api_all():
#     return jsonify(books)
#
# @simple.route('/api/v1/resources/books', methods=['GET'])
# def api_id():# Check if an ID was provided as part of the URL.
#     # If ID is provided, assign it to a variable.
#     # If no ID is provided, display an error in the browser.
#     if 'id' in request.args:
#         id = int(request.args['id'])
#     else:
#         return "Error: No id field provided. Please specify an id."# Create an empty list for our results
#     results = []# Loop through the data and match results that fit the requested ID.
#     # IDs are unique, but other fields might return many results
#     for book in books:
#         if book['id'] == id:
#             results.append(book)# Use the jsonify function from Flask to convert our list of
#     # Python dictionaries to the JSON format.
#     return jsonify(results)
#
# @simple.route('/api/add_message/<uuid>', methods=['GET', 'POST'])
# def add_message(uuid):
#     # content = request.json
#     # print(content)
#     return jsonify({"uuid":uuid})
#
#
# @simple.route('/api/ville/<ville>', methods=['GET'])
# def ville(ville):
#     return jsonify({"ville":ville})
