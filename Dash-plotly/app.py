import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from plotly import tools
from dash.dependencies import Input, Output
import numpy as np
from categoryPlot import getPlot, dfUkAccident

app = dash.Dash(__name__)
server = app.server # make python obj with Dash() method

app.title = 'UK Accident Dashboard'; # set web title
dfTable = dfUkAccident
#the layout/content
app.layout = html.Div(children=[
    dcc.Tabs(id="tabs", value='tab-1', 
        style={
            'fontFamily': 'system-ui'
        },
        content_style={
            'fontFamily': 'Arial',
            'borderLeft': '1px solid #d6d6d6',
            'borderRight': '1px solid #d6d6d6',
            'borderBottom': '1px solid #d6d6d6',
            'padding': '44px'
        }, 
        children=[
            dcc.Tab(label='Data UK Accident', value='tab-1', children=[
                html.Div([ 
                    html.Table([      
                    ],style={ 'width': '300px', 'paddingBottom': '20px' }),
                    html.Div(id='divTable', children=[
                        html.H1('Table UK Data Accident'),
                        html.H4(['Total Row : ' + str(len(dfTable))]),
                        dcc.Graph(
                            id='tableData',
                            figure= {
                                'data': [
                                    go.Table(
                                        header=dict(
                                            values=['<b>'+ col +'</b>' for col in dfTable.columns],
                                            font = dict(size = 14),
                                            height = 30,
                                            fill = dict(color='#a1c3d1')
                                        ),
                                        cells=dict(
                                            values=[dfTable[col] for col in dfTable.columns],
                                            font = dict(size = 12),
                                            height = 30,
                                            fill = dict(color='#EDFAFF'),
                                            align = ['right']
                                        )
                                    )
                                ],
                                'layout': dict(height=500,margin={'l': 0, 'b': 40, 't': 10, 'r': 0})
                            }
                        )
                    ])
                ])
            ]),
            dcc.Tab(label='Categorical Plot', value='tab-2', children=[
                html.Div([
                    html.H1('Categorical Plot Ujian Titanic'),
                    html.Table([
                        html.Tr([
                            html.Td([
                                html.P('Jenis : '),
                                dcc.Dropdown(
                                    id='ddl-jenis-plot-category',
                                    options=[{'label': 'Bar', 'value': 'bar'},
                                            {'label': 'Violin', 'value': 'violin'},
                                            {'label': 'Box', 'value': 'box'}],
                                    value='bar'
                                )
                            ]),
                            html.Td([
                                html.P('X Axis : '),
                                dcc.Dropdown(
                                    id='ddl-x-plot-category',
                                    options=[{'label': 'Sex_of_Driver', 'value': 'Sex_of_Driver'},
                                            {'label': 'Light_Conditions', 'value': 'Light_Conditions'},
                                            {'label': 'Road_Type', 'value': 'Road_Type'},
                                            {'label': 'Day_of_Week', 'value': 'Day_of_Week'},
                                            {'label': 'Vehicle_Type', 'value': 'Vehicle_Type'},
                                            {'label': 'High_Risk', 'value': 'High_Risk'}],
                                    value='Sex_of_Driver'
                                )
                            ])
                        ])
                    ], style={ 'width' : '700px', 'margin': '0 auto'}),
                    dcc.Graph(
                        id='categoricalPlot',
                        figure={
                            'data': []
                        }
                    )
                ])
            ])
    ])
], 
style={
    'maxWidth': '1200px',
    'margin': '0 auto'
});


@app.callback(
    Output('categoricalPlot', 'figure'),
    [Input('ddl-jenis-plot-category', 'value'),
    Input('ddl-x-plot-category', 'value')])
def update_category_graph(ddljeniscategory, ddlxcategory):
    return {
            'data': getPlot('jointable', ddljeniscategory,ddlxcategory),
            'layout': go.Layout(
                xaxis={'title': ddlxcategory.capitalize()}, yaxis={'title': 'Speed Limit (Km/h), Age (Year)'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1.2}, hovermode='closest',
                boxmode='group',violinmode='group'
                # plot_bgcolor= 'black', paper_bgcolor= 'black',
            )
    };

if __name__ == '__main__':
    # run server on port 1997
    # debug=True for auto restart if code edited
    app.run_server(debug=True, port=1997) 

