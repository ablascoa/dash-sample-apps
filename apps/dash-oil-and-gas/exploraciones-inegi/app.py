import dash
import pandas as pd
import pathlib
import dash_core_components as dcc
import dash_html_components as html
from stacked_barchart_layout import fig as stacked_fig


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


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
                        '''),
                       dcc.Graph(figure=dict(
                           data=[
                               dict(
                                   x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                                      2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                                   y=[219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                                      350, 430, 474, 526, 488, 537, 500, 439],
                                   name='Rest of world',
                                   marker=dict(
                                       color='rgb(55, 83, 109)'
                                   )
                               ),
                               dict(
                                   x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                                      2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                                   y=[16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                                      299, 340, 403, 549, 499],
                                   name='China',
                                   marker=dict(
                                       color='rgb(26, 118, 255)'
                                   )
                               )
                           ],
                           layout=dict(
                               title='US Export of Plastic Scrap',
                               showlegend=True,
                               legend=dict(
                                   x=0,
                                   y=1.0
                               ),
                               margin=dict(l=40, r=0, t=40, b=30)
                           )
                       ), style={'height': 300}, id='my-graph'),
                       dcc.Graph()
                       ])


# Main
if __name__ == "__main__":
    app.run_server(debug=True)
