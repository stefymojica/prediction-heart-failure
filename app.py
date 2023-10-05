from dash import Dash, html, dcc

model = ('../prediction/model.pkl')

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='Prediction Heart Failure'),

    html.Br(),
    html.Label('Age'),
    dcc.Input(value='Anote age', type='number'),

    html.Br(),
    html.Label('Anaemia'),
    dcc.Input(value='Anote anaemia', type='number'),

    html.Br(),
    html.Label('Diabetes'),
    dcc.Input(value='Anote Diabetes', type='number'),

    html.Br(),
    html.Label('Ejection fraction'),
    dcc.Input(value='Anote Ejection fraction', type='number'),

    html.Br(),
    html.Label('High blood pressure'),
    dcc.Input(value='Anote High blood pressure', type='number'),

    html.Br(),
    html.Label('Serum creatinine'),
    dcc.Input(value='Anote Serum creatinine', type='number'),

    html.Br(),
    html.Label('Sex'),
    dcc.Input(value='Anote Sex', type='number'),

    html.Br(),
    html.Label('Smoking'),
    dcc.Input(value='Anote Smoking', type='number'),
])

app.run(debug=True, port=8060)
if __name__ == '__main__':
    app.run(debug=True)
