# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html, Input, Output, State
import plotly.express as px
import pandas as pd
from dash import dash_table

app = Dash(__name__)

df = pd.read_csv("dash/wine_quality.csv")

columnList = df.columns.values.tolist()


app.layout = html.Div(
    [
    dash_table.DataTable(
        data = df.head(10).to_dict('records'),
        columns = [{"name": i, "id": i} for i in df.columns],
        id='data-frame-table'
        ),
    dcc.Dropdown(
        options = [
            {'label' : 'Regression', 'value': 'pH'},
            {'label':'Classification','value': 'target'}
        ],
        id = 'model-chooser',
        clearable = False
        ),
    dcc.Dropdown(
        id = 'second-param-chooser',
        clearable = False
        ),
    html.Div(
        id='fig-container',
        children=[]
        )
    ],
    id ='app-container'
    )

@app.callback(
    Output('second-param-chooser','options'),
    Input('model-chooser', 'value')
    )
def display_dropdowns(value):
    ## if 'Regression' -> nie ma do wyboru 'pH'
    ## if 'Classification' -> nie ma do wyboru 'target'
    return [colName for colName in columnList if colName != value]

@app.callback(
    Output('fig-container','children'),
    Input('second-param-chooser', 'value')
    )
def display_graph(value):
    # nie działa dynamiczne wstawianie zmiennej 'x', wpisane na sztywno 'chlorides'
    fig = px.scatter(df, x = 'chlorides',y=value)
    return [dcc.Graph(figure=fig)]


if __name__ == '__main__':
    app.run_server(debug=True)
