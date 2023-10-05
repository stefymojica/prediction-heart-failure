from dash import Dash, html

model = ('../prediction/model.pkl')

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='Prediction Heart Failure')
])

app.run(debug=True, port=8060)
if __name__ == '__main__':
    app.run(debug=True)
