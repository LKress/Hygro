import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt
import os

from dash.dependencies import Input, Output

import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#1e212f',
    'background-dark': '#171a27',
    'text': '#ffffff',
    'temp-col': '#d44a2f'
}

app.title = 'Hygrometer'
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.Br(),
    html.Center(
    dcc.Tabs([
        dcc.Tab(disabled_style={"color": "#ffffff", 'background': '#1e45f2',}, selected_style={"color": "#ffffff", 'background':'#171a27'}, id="temp-tab", label='Temp', children=[

            html.Center(
                html.H1(
                    children='Temperatur',
                    style={
                        'textAlign': 'center',
                        'color': colors['text']
                        }
                )
            ),

            html.Center(
                html.Div(style={'width': '97%'}, children=[
                    dcc.Graph(style={'color': colors['temp-col']}, id='temp-graphic'),
                    ]
                    ),
            ),

            html.Br(),

            html.Center(
                html.Button('Aktualisieren', id='btn-nclicks-1', n_clicks=0)
            ),

            html.Br()

        ]),
        dcc.Tab(disabled_style={"color": "#ffffff", 'background': '#1e45f2',}, selected_style={"color": "#ffffff", 'background':'#171a27'}, label='Hum', children=[

            html.H1(
                children='Luftfeuchtigkeit',
                style={
                    'textAlign': 'center',
                    'color': colors['text']
                }
            ),

            html.Center(
                html.Div(style={'width': '97%'}, children=[
                    dcc.Graph(style={'color': colors['temp-col']}, id='hum-graphic'),
                ])
            ),

            html.Br(),

            html.Center(
                html.Button('Aktualisieren', id='btn-nclicks-2', n_clicks=0)
            ),
            html.Br()

        ]),
        dcc.Tab(disabled_style={"color": "#ffffff", 'background': '#1e45f2',}, selected_style={"color": "#ffffff", 'background':'#171a27'}, label='Press', children=[

            html.H1(
                children='Luftdruck',
                style={
                    'textAlign': 'center',
                    'color': colors['text']
                }
            ),

            html.Center(
                html.Div(style={'width': '97%'}, children=[
                    dcc.Graph(style={'color': colors['temp-col']}, id='press-graphic'),
                ])
            ),

            html.Br(),

            html.Center(
                html.Button('Aktualisieren', id='btn-nclicks-3', n_clicks=0)
            ),
            html.Br()
        ])
    ], colors={
#        "border": "#171a27",
#        "primary": "#6e6e6e",
#        "background": "#171a27",
#        "border-bottom-color": "#10f49f"
    }, style={
        "width": "97%"
    }

    ))
])


@app.callback(
    Output('temp-graphic', 'figure'),
    [Input('btn-nclicks-1', 'n_clicks')]
)
def update_temp(btn1):
    data = pd.read_csv("data.tsv")
    return{
        'data':[
            dict(
                type='line',
                mode='line',
                name='temperatur',
                x=data.time,
                y=data.temp,
                line=dict(
                    #shape="spline",
                    #smoothing=2,
                    width=3,
                    color='#ff583b'
                ),
                marker=dict(symbol='diamond-open')
            )
        ],
        'layout': {
            'plot_bgcolor': colors['background-dark'],
            'paper_bgcolor': colors['background-dark'],
            'font': {
                'color': colors['text']
            }
        }
    }

@app.callback(
    Output('hum-graphic', 'figure'),
    [Input('btn-nclicks-2', 'n_clicks')]
    )
def update_hum(btn2):
    data = pd.read_csv("data.tsv")
    return{
        'data':[
            dict(
                type='line',
                mode='line',
                name='luftfeuchtigkeit',
                x=data.time,
                y=data.hum,
                line=dict(
                    #shape="spline",
                    #smoothing=2,
                    width=3,
                    color='#4f7eff'
                ),
                marker=dict(symbol='diamond-open')
            )
        ],
        'layout': {
            'plot_bgcolor': colors['background-dark'],
            'paper_bgcolor': colors['background-dark'],
            'font': {
                'color': colors['text']
            }
        }
    }

@app.callback(
    Output('press-graphic', 'figure'),
    [Input('btn-nclicks-3', 'n_clicks')]
    )
def update_temp(btn3):
    data = pd.read_csv("data.tsv")
    return{
        'data':[
            dict(
                type='line',
                mode='line',
                name='luftdruck',
                x=data.time,
                y=data.press,
                line=dict(
                    #shape="spline",
                    #smoothing=2,
                    width=3,
                    color='#03a600'
                ),
                marker=dict(symbol='diamond-open')
            )
        ],
        'layout': {
            'plot_bgcolor': colors['background-dark'],
            'paper_bgcolor': colors['background-dark'],
            'font': {
                'color': colors['text']
            }
        }
    }


if __name__ == '__main__':
    app.run_server(debug=False, port=8080, host='0.0.0.0')
