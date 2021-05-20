from WebApp.mainapp import app
import dash_html_components as html
import flask
from REST_API.rest_api import API
from WebApp.Layout import Layout

app.layout = Layout()
app.server.register_blueprint(API)

if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0', port=90)
