from flask import Blueprint, jsonify, request, Response, render_template
import pandas as pd
import json


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
        return Response("Combination not found", status=404)
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


# View elements by id

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



