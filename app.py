import dash
import dash_html_components as html
import flask
from REST_API.rest_api import API

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__)


app.layout = html.Div()

app.server.register_blueprint(API)



app.run_server(debug=False, host='0.0.0.0',port=90)