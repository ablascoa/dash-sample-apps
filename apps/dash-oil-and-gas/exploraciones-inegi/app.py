import dash
import pandas as pd
import pathlib
import dash_core_components as dcc
import dash_html_components as html


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)

# get relative data folder
PATH = pathlib.Path(__file__).parent
print(PATH)
DATA_PATH = PATH.joinpath("data").resolve()

app = dash.Dash(
    __name__, meta_tags=[
        {"name": "viewport", "content": "width=device-width"}],
    external_stylesheets=external_stylesheets
)
server = app.server


app.layout = html.Div([html.H3('Prueba'),
                       html.H1('Hello Dash'),
                       html.Div([html.P('Dash converts Python classes into HTML'),
                                 html.P(
                           "This conversion happens behind the scenes by Dash's JavaScript front-end")
                       ]),
                       dcc.Markdown('''
                        #### Dash and Markdown

                        Dash supports [Markdown](http://commonmark.org/help).

                        Markdown is a simple way to write and format text.
                        It includes a syntax for things like **bold text** and *italics*,
                        [links](http://commonmark.org/help), inline `code` snippets, lists,
                        quotes, and more.
                        ''')
                       ])


# Main
if __name__ == "__main__":
    app.run_server(debug=True)
