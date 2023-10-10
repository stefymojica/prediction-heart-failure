from dash import Dash, html, dcc, callback, Output, Input
import pickle
from sklearn.neural_network import MLPClassifier

model = 'src/prediction/model.pkl'
with open(model, 'rb') as file:
    model = pickle.load(file)

app = Dash(__name__)

app.layout = html.Div([
    html.Div(
        style={
            'display': 'flex',
            'flexDirection': 'column',
            'alignItems': 'center',
            'justifyContent': 'center',
            'margin-bottom': '30px'
        },  children=[
            html.H1(
                children='Prediction Heart Failure',
                style={
                    'textAlign': 'center',
                    'color': '#113f67'})
        ]),
    html.Div(
        style={
            'display': 'grid',
            'grid-template-columns': '1fr 1fr',
        }, children=[
            html.Div(
                style={
                    'display': 'flex',
                    'flexDirection': 'column',
                    'margin-left': '370px',
                    'alignItems': 'left',
                    'justifyContent': 'center'
                },
                children=[
                    html.Br(),
                    html.Label('Age'),
                    dcc.Input(id='my-input-1', value='Anote Age', type='number',
                              style={
                                  'textAlign': 'center',
                                  'margin-bottom': '10px',
                                  'width': '150px'}),

                    html.Br(),
                    html.Label('Anaemia'),
                    # dcc.Dropdown(id='my-input-2',
                    #              options=['O', '1'],
                    #              value='Anote anaemia',
                    #              style={
                    #                  'textAlign': 'center',
                    #                  'margin-bottom': '10px',
                    #                  'width': '160px'}
                    #              ),
                    dcc.Input(id='my-input-2', value='Anote Anaemia', type='number',
                              style={
                                  'textAlign': 'center',
                                  'margin-bottom': '10px',
                                  'width': '150px'}),

                    html.Br(),
                    html.Label('Diabetes'),
                    # dcc.Dropdown(id='my-input-3',
                    #              options=['O', '1'],
                    #              value='Anote Diabetes',
                    #              style={
                    #                  'textAlign': 'center',
                    #                  'margin-bottom': '10px',
                    #                  'width': '160px'}
                    #              ),
                    dcc.Input(id='my-input-3', value='Anote Diabetes', type='number',
                              style={
                                  'textAlign': 'center',
                                  'margin-bottom': '10px',
                                  'width': '150px'}),

                    html.Br(),
                    html.Label('Ejection fraction'),
                    dcc.Input(id='my-input-4', value='Anote Ejection fraction', type='number',
                              style={
                                  'textAlign': 'center',
                                  'margin-bottom': '10px',
                                  'width': '150px'}),
                ]),
            html.Div(
                style={
                    'display': 'flex',
                    'flexDirection': 'column',
                    'margin-left': '150px',
                    'alignItems': 'left',
                    'justifyContent': 'left',
                },
                children=[
                    html.Br(),
                    html.Label('High blood pressure'),
                    # dcc.Dropdown(id='my-input-5',
                    #              options=['O', '1'],
                    #              value='Anote High blood pressure',
                    #              style={
                    #                  'textAlign': 'center',
                    #                  'margin-bottom': '10px',
                    #                  'width': '160px'}
                    #              ),
                    dcc.Input(id='my-input-5', value='Anote High blood pressure', type='number',
                              style={
                                  'textAlign': 'center',
                                  'margin-bottom': '10px',
                                  'width': '150px'}),

                    html.Br(),
                    html.Label('Serum creatinine'),
                    dcc.Input(id='my-input-6', value='Anote Serum creatinine', type='number',
                              style={
                                  'textAlign': 'center',
                                  'margin-bottom': '10px',
                                  'width': '150px'}),
                    html.Br(),
                    html.Label('Sex'),
                    # dcc.Dropdown(id='my-input-7',
                    #              options=['O', '1'],
                    #              value='Sex',
                    #              style={
                    #                  'textAlign': 'center',
                    #                  'margin-bottom': '10px',
                    #                  'width': '160px'}
                    #              ),
                    dcc.Input(id='my-input-7', value='Anote Sex', type='number',
                              style={
                                  'textAlign': 'center',
                                  'margin-bottom': '10px',
                                  'width': '150px'}),

                    html.Br(),
                    html.Label('Smoking'),
                    # dcc.Dropdown(id='my-input-8',
                    #              options=['O', '1'],
                    #              value='Smoking',
                    #              style={
                    #                  'textAlign': 'center',
                    #                  'margin-bottom': '10px',
                    #                  'width': '160px'}
                    #              ),
                    dcc.Input(id='my-input-8', value='Anote Smoking', type='number',
                              style={
                                  'textAlign': 'center',
                                  'margin-bottom': '10px',
                                  'width': '150px'}),
                ])
        ]),
    html.Div(
        style={
            'textAlign': 'center',
            'margin-top': '70px'
        }, children=[
            html.Button('Click here to see the result', id='show-secret'),
            html.Div(id='resultado')
        ])
])


@callback(
    Output('resultado', 'children'),
    Input('show-secret', 'n_clicks'),
    [Input('my-input-1', 'value'), Input('my-input-2', 'value'),
     Input('my-input-3', 'value'), Input('my-input-4', 'value'),
     Input('my-input-4', 'value'), Input('my-input-5', 'value'),
     Input('my-input-7', 'value'), Input('my-input-8', 'value')]
)
def do_prediction(n_clicks, value1, value2, value3, value4, value5, value6, value7, value8):
    if n_clicks is None:
        return None
    predicts = model.predict(
        [[value1, value2, value3, value4, value5, value6, value7, value8]])

    if predicts[0] == 0:
        return "Negativo"

    else:
        return "Positivo"


if __name__ == '__main__':
    app.run(debug=True,  port=8080)
