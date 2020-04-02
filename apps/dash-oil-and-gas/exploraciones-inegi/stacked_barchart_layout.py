import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

pib_prim = pd.read_csv('data/PIB_primario.csv')
pib_sec = pd.read_csv('data/PIB_secundario.csv')
pib_ter = pd.read_csv('data/PIB_terciario.csv')

print('hola')

entidades = [col for col in pib_prim.columns.values if col != 'Periodo']
print(entidades)

app = dash.Dash(__name__)

dates = ['2016-04-01', '2016-07-01', '2016-10-01']
trace1 = go.Bar(
    x=dates, y=[20, 14, 23],
    name='Brn'
)
trace2 = go.Bar(
    x=dates, y=[12, 18, 29],
    name='Wrl'
)
trace3 = go.Bar(
    x=dates, y=[20, 5, 12],
    name='Lpl'
)
trace4 = go.Bar(
    x=dates, y=[3, 18, 4],
    name='HNE'
)
trace5 = go.Bar(
    x=dates, y=[12, 3, 29],
    name='Zoo'
)

data = [trace1, trace2, trace3, trace4, trace5]
layout = go.Layout(
    barmode='stack',
    xaxis=dict(tickvals=['2016-04-01', '2016-07-01', '2016-10-01'])
)

fig = go.Figure(data=data, layout=layout)


app.layout = html.Div([
    html.Div(
        dcc.Graph(figure=fig)
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
