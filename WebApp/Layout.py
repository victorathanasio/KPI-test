import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash_table
import pandas as pd
from WebApp.mainapp import app
import json

df = pd.read_json('dataset.json')
df = df[['ville', 'etat_d_avancement', 'titreoperation', 'mandataire', 'lycee', 'codeuai',
         'entreprise', 'maitrise_d_oeuvre', 'ppi', 'notification_du_marche', 'annee_de_livraison',
         'cao_attribution', 'longitude', 'montant_des_ap_votes_en_meu', 'latitude', 'mode_de_devolution',
         'annee_d_individualisation', 'enveloppe_prev_en_meu', 'nombre_de_lots']]


def Layout():
    return html.Div([
        html.P("Welcome to the KPI case !",
               style={'font-size': '36px'}),

        html.P("The table in editable and filtrable, give it a try !",
               style={'font-size': '16px'}),

        dash_table.DataTable(
            columns=[
                {'name': 'codeuai', 'id': 'codeuai', 'type': 'text', 'hideable': 'True'},
                {'name': 'Ville', 'id': 'ville', 'type': 'text', 'hideable': 'True'},
                {'name': "État d'avancement", 'id': 'etat_d_avancement', 'type': 'text', 'hideable': 'True'},
                {'name': 'Titre opération', 'id': 'titreoperation', 'type': 'text', 'hideable': 'True'},
                {'name': 'Mandataire', 'id': 'mandataire', 'type': 'text', 'hideable': 'True'},
                {'name': 'lycée', 'id': 'lycee', 'type': 'text', 'hideable': 'True'},
                {'name': 'Entreprise', 'id': 'entreprise', 'type': 'text', 'hideable': 'True'},
                {'name': "Maitrise d'oeuvre", 'id': 'maitrise_d_oeuvre', 'type': 'text', 'hideable': 'True'},
                {'name': 'ppi', 'id': 'ppi', 'type': 'text', 'hideable': 'True'},
                {'name': 'Notification du marche', 'id': 'notification_du_marche', 'type': 'text', 'hideable': 'True'},
                {'name': 'Année de livraison', 'id': 'annee_de_livraison', 'type': 'text', 'hideable': 'True'},
                {'name': 'Cao attribution', 'id': 'cao_attribution', 'type': 'text', 'hideable': 'True'},
                {'name': 'Latitude', 'id': 'latitude', 'type': 'text', 'hideable': 'True'},
                {'name': 'Longitude', 'id': 'longitude', 'type': 'text', 'hideable': 'True'},
                {'name': 'Montant des ap votes en meu', 'id': 'montant_des_ap_votes_en_meu', 'type': 'text',
                 'hideable': 'True'},
                {'name': 'Mode de dévolution', 'id': 'mode_de_devolution', 'type': 'text', 'hideable': 'True'},
                {'name': "Année d'individualisation", 'id': 'annee_d_individualisation', 'type': 'text',
                 'hideable': 'True'},
                {'name': 'Enveloppe prev en meu', 'id': 'enveloppe_prev_en_meu', 'type': 'text', 'hideable': 'True'},
                {'name': 'Nombre de lots', 'id': 'nombre_de_lots', 'type': 'text', 'hideable': 'True'}
            ],
            data=df.to_dict('records'),
            editable=True,
            filter_action='native',
            sort_action='native',
            style_table={
                'height': 400,
                'overflowX': 'auto'

            },
            style_data={
                'width': '150px',
                'minWidth': '150px',
                'maxWidth': '150px',
                'height': 'auto'
            },
            style_cell={
                'minHeight': '50px',
                'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                'whiteSpace': 'normal'
            },
            fixed_columns={'headers': True, 'codeuai': 1},
            id='Table'
        ),

        dbc.Button('Submit changes', id='submit', size="lg"),

        dbc.Button('Open in new window', id='new_window', size="lg"),

        dcc.ConfirmDialog(
            id='confirm',
            message='Dataset updated !!',
        ),

        dcc.Location(id='url', refresh=True)

    ])


@app.callback([Output('confirm', 'displayed'),
               Output('Table', 'data')],
              Input('submit', 'n_clicks'),
              State('Table', 'data'))
def display_confirm(n_clicks, table):
    df = pd.read_json('dataset.json')
    df = df[['ville', 'etat_d_avancement', 'titreoperation', 'mandataire', 'lycee', 'codeuai',
             'entreprise', 'maitrise_d_oeuvre', 'ppi', 'notification_du_marche', 'annee_de_livraison',
             'cao_attribution', 'longitude', 'montant_des_ap_votes_en_meu', 'latitude', 'mode_de_devolution',
             'annee_d_individualisation', 'enveloppe_prev_en_meu', 'nombre_de_lots']]
    if n_clicks is None:
        return False, df.to_dict('records')
    else:
        with open('dataset.json', 'w') as outfile:
            json.dump(table, outfile)
        return True, df.to_dict('records')


@app.callback(Output('url', 'pathname'),
              Input('new_window', 'n_clicks'),
              State('Table', 'active_cell'),
              State('Table', 'derived_virtual_data'),
              State('Table', 'data')
              )
def go_to_single_view(n_clicks, active_cell, derived_data, data):
    if n_clicks is not None:
        desired_row = pd.DataFrame(derived_data).iloc[active_cell['row']].dropna().to_dict()
        data = pd.DataFrame(data)
        for key in desired_row:
            data = data[data[key] == desired_row[key]]
        index = data.index[0]
        return '/single_view/{}'.format(index)
    else:
        return '/'


