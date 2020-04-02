import dash
import dash_core_components as dcc
# Graficar PIB primario, secundario y terciario (como porcentajes del nacional)
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import json
import pandas as pd
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# TODO: automatizar la manera años
start_year = 2000
end_year = 2018


def create_pib_pct_df(df, total_column_label='Total nacional'):
    """
    dado un DataFrame y una columna de totales, divide todas las columnas para
    obtener porcentajes
    total_column_label: name of the column with the total values
    """
    df_pct = df.div(df.loc[:, total_column_label], axis=0)*100
    return df_pct


def create_pib_trace(df, year, total_column_label='Total nacional'):
    # sector = 'prim' |'sec' | 'ter'
    x = [col for col in df.columns.values if col != total_column_label]
    y = df.loc[year, x]
    trace = go.Bar(x=x, y=y)
    return trace


path_to_data = '../'

pib_dict = dict(
    prim=dict(file='PIB_primario.csv', label='Sector primario'),
    sec=dict(file='PIB_secundario.csv', label='Sector secundario'),
    ter=dict(file='PIB_terciario.csv', label='Sector terciario'),
)


# create dataframes dict (by importing their files)
dfs = {}
for sector in pib_dict.keys():
    file = pib_dict[sector]['file']
    df = pd.read_csv(f'{path_to_data}data/{file}', index_col=0)
    dfs[sector] = dict(df=df)


app.layout = html.Div([
    html.Div(
        [dcc.Dropdown(
            id='pib-pct-edos-1-sectores',
            options=[{'label': pib_dict[sector]['label'], 'value': sector}
                     for sector in pib_dict.keys()],
            multi=True,
            value=[sector for sector in pib_dict.keys()]
        ),
            dcc.Dropdown(
            id='pib-pct-edos-1-year',
            options=[{'label': str(year), 'value': year}
                     for year in range(start_year, end_year)],
            value=end_year
        ),
            dcc.Graph(id='pib-pct-edos-1'),
            dcc.Input(id='my-id', value='initial value', type='text'),
            html.Div(id='my-div')
        ]

    )
])


@app.callback(Output(component_id='pib-pct-edos-1', component_property='figure'),
              [Input(component_id='pib-pct-edos-1-sectores', component_property='value'),
               Input(component_id='pib-pct-edos-1-year', component_property='value')])
def create_pib_pct_graph(sectors_array, year):
    """crea una gráfica de porcentajes de aportación al pib para los
    sectores indicados en el array y el año especificado
    sectores_array=['prim', 'sec', 'ter'] --> se puede elegir uno o más
    """
    if (sectors_array is None or year is None or len(sectors_array) == 0):
        return go.Figure(data=[], layout=go.Layout())

    # create totals dataframe
    print(sectors_array)
    totals = pd.DataFrame(np.zeros((dfs[sectors_array[0]]['df']).shape),
                          index=dfs[sectors_array[0]]['df'].index,
                          columns=dfs[sectors_array[0]]['df'].columns)
    for sector in sectors_array:
        totals = totals + dfs[sector]['df']

    # create pib pct df from totals dataframe
    totals_pct = create_pib_pct_df(totals)

    # create trace
    totals_pct_trace = create_pib_trace(totals_pct, year)
    data = [totals_pct_trace]
    # create layout
    layout = go.Layout(
        xaxis=dict(tickmode='linear', categoryorder='total descending')
    )
    # create figure
    fig = go.Figure(data=data, layout=layout)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
