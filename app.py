from dash import Dash, html, dcc

model = ('../prediction/model.pkl')

app = Dash(__name__)

app.layout = html.Div([
    html.Div(
        style={
        'display': 'flex',
        'flexDirection': 'column',
        'alignItems': 'center',
        'justifyContent': 'center'
    },  children=[
        html.H1(
            children='Prediction Heart Failure',
            style={
                'textAlign': 'center',
                'color': '#113f67'})
    ]),
    html.Div([
        html.Div(
            style={
                'display': 'flex',
                'flexDirection': 'column',
                'margin-left': '400px',
                'alignItems': 'left',
                'justifyContent': 'center'
                },
            children=[
        html.Br(),
        html.Label('Age'),
        dcc.Input(value='Anote Age', type='number',
                style={
                    'textAlign': 'center',
                    'margin-bottom': '10px',
                    'width': '150px'}),

        html.Br(),
        html.Label('Anaemia'),
        dcc.Input(value='Anote Anaemia', type='number',
                style={
                    'textAlign': 'center',
                    'margin-bottom': '10px',
                    'width': '150px'}),

        html.Br(),
        html.Label('Diabetes'),
        dcc.Input(value='Anote Diabetes', type='number',
                style={
                    'textAlign': 'center',
                    'margin-bottom': '10px',
                    'width': '150px'}),

        html.Br(),
        html.Label('Ejection fraction'),
        dcc.Input(value='Anote Ejection fraction', type='number',
                style={
                    'textAlign': 'center',
                    'margin-bottom': '10px',
                    'width': '150px'}),
    ]),
        html.Div(
            style={
                'display': 'flex',
                'flexDirection': 'column',
                'margin-left': '750px',
                'alignItems': 'left',
                'justifyContent': 'left',
                'margin-top':'-273px',
                },
            children=[
        html.Br(),
        html.Label('High blood pressure'),
        dcc.Input(value='Anote High blood pressure', type='number',
                style={
                    'textAlign': 'center',
                    'margin-bottom': '10px',
                    'width': '150px'}),

        html.Br(),
        html.Label('Serum creatinine'),
        dcc.Input(value='Anote Serum creatinine', type='number',
                style={
                    'textAlign': 'center',
                    'margin-bottom': '10px',
                    'width': '150px'}),

        html.Br(),
        html.Label('Sex'),
        dcc.Input(value='Anote Sex', type='number',
                style={
                    'textAlign': 'center',
                    'margin-bottom': '10px',
                    'width': '150px'}),

        html.Br(),
        html.Label('Smoking'),
        dcc.Input(value='Anote Smoking', type='number',
                style={
                    'textAlign': 'center',
                    'margin-bottom': '10px',
                    'width': '150px'}),
    ])
    ])
    ])



app.run(debug=True, port=8060)
if __name__ == '__main__':
    app.run(debug=True)
