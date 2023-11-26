import pickle
import numpy as np
from dash import Dash, html, dcc, callback, Output, Input
from sklearn.neural_network import MLPClassifier

# import model pkl

model = 'exercise/model.pkl'
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
            'margin-bottom': '10px'
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
                    'margin-left': '630px',
                    'alignItems': 'left',
                    'justifyContent': 'center'
                },
                children=[
                    html.Br(),
                    html.Label('Age',
                            style={
                                'color': '#113f67',
                                'font-size': '20',
                                'font-weight': 'bold'}),
                    dcc.Input(id='my-input-1', value='Anote Age', type='number',
                            style={
                                'textAlign': 'center',
                                'margin-bottom': '10px',
                                'width': '150px',
                                'border-radius': '10px',
                                'border-color': '#53a8b6',
                                'border-width': 'thick'}),

                    html.Br(),
                    html.Label('Anaemia',
                            style={
                                'color': '#113f67',
                                'font-size': '20',
                                'font-weight': 'bold'}),
                    dcc.Input(id='my-input-2', value='Anote Anaemia', type='number',
                            style={
                                'textAlign': 'center',
                                'margin-bottom': '10px',
                                'width': '150px',
                                'border-radius': '10px',
                                'border-color': '#53a8b6',
                                'border-width': 'thick'}),

                    html.Br(),
                    html.Label('Diabetes',
                            style={
                                'color': '#113f67',
                                'font-size': '20',
                                'font-weight': 'bold'}),
                    dcc.Input(id='my-input-3', value='Anote Diabetes', type='number',
                            style={
                                'textAlign': 'center',
                                'margin-bottom': '10px',
                                'width': '150px',
                                'border-radius': '10px',
                                'border-color': '#53a8b6',
                                'border-width': 'thick'}),

                    html.Br(),
                    html.Label('Ejection fraction',
                            style={
                                'color': '#113f67',
                                'font-size': '20',
                                'font-weight': 'bold'}),
                    dcc.Input(id='my-input-4', value='Anote Ejection fraction', type='number',
                            style={
                                'textAlign': 'center',
                                'margin-bottom': '10px',
                                'width': '150px',
                                'border-radius': '10px',
                                'border-color': '#53a8b6',
                                'border-width': 'thick'}),
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
                    html.Label('High blood pressure',
                            style={
                                'color': '#113f67',
                                'font-size': '20',
                                'font-weight': 'bold'}),
                    dcc.Input(id='my-input-5', value='Anote High blood pressure', type='number',
                            style={
                                'textAlign': 'center',
                                'margin-bottom': '10px',
                                'width': '150px',
                                'border-radius': '10px',
                                'border-color': '#53a8b6',
                                'border-width': 'thick'}),

                    html.Br(),
                    html.Label('Serum creatinine',
                            style={
                                'color': '#113f67',
                                'font-size': '20',
                                'font-weight': 'bold'}),
                    dcc.Input(id='my-input-6', value='Anote Serum creatinine', type='number',
                            style={
                                'textAlign': 'center',
                                'margin-bottom': '10px',
                                'width': '150px',
                                'border-radius': '10px',
                                'border-color': '#53a8b6',
                                'border-width': 'thick'}),
                    html.Br(),
                    html.Label('Sex',
                            style={
                                'color': '#113f67',
                                'font-size': '20',
                                'font-weight': 'bold'}),
                    dcc.Input(id='my-input-7', value='Anote Sex', type='number',
                            style={
                                'textAlign': 'center',
                                'margin-bottom': '10px',
                                'width': '150px',
                                'border-radius': '10px',
                                'border-color': '#53a8b6',
                                'border-width': 'thick'}),

                    html.Br(),
                    html.Label('Smoking',
                            style={
                                'color': '#113f67',
                                'font-size': '20',
                                'font-weight': 'bold'}),
                    dcc.Input(id='my-input-8', value='Anote Smoking', type='number',
                            style={
                                'textAlign': 'center',
                                'margin-bottom': '10px',
                                'width': '150px',
                                'border-radius': '10px',
                                'border-color': '#53a8b6',
                                'border-width': 'thick'}),
                ])
        ]),
    html.Div(
        style={
            'textAlign': 'center',
            'margin-top': '70px'
        }, children=[
            html.Button('Click here to see the result', id='show-secret',
                        style={
                            'background-color': 'white',
                            'color': '#113f67',
                            'textAlign': 'center',
                            'margin-bottom': '10px',
                            'width': '150px',
                            'border-radius': '10px',
                            'border-color': '#53a8b6',
                            'border-width': 'thick'}),
            html.Div(id='resultado',
                    style={
                        'margin-top': '10px',
                        'color': '#38598b',
                        'font-size': '35px',
                        'font-weight': 'bold'
                    })
        ])
])

# @callback

@callback(
    Output('resultado','children'),
    Input('show-secret','n_clicks'),
    [Input('my-input-1', 'value'),Input('my-input-2', 'value'),
    Input('my-input-3', 'value'), Input('my-input-4', 'value'),
    Input('my-input-5', 'value'), Input('my-input-6', 'value'),
    Input('my-input-7', 'value'), Input('my-input-8', 'value')]
)

# def main()

def main(n_clicks,value1,value2, value3, value4, value5, value6, value7, value8):
    return None if n_clicks is None else do_prediction(value1,value2, value3, value4, value5, value6, value7, value8)

# def do_prediction()

def do_prediction(value1,value2, value3, value4, value5, value6, value7, value8):
    value = np.asarray([value1,value2, value3, value4, value5, value6, value7, value8]
    ).reshape(1,-1)
    predict = model.predict(value)
    return "Negative" if predict[0] == 0 else "Positive"

if __name__ == '__main__':
    app.run(debug=True,  port=8080)
