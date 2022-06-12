from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('data/output.csv')

fig = px.line(df, x="date", y="sales", color="region")

app.layout = html.Div(children=[
    html.H1(children="Sales Price", style={"backgroundColor": "#161A1D", "color": "#2178BC", "textAlign": 'center'}),
    
    html.Div([
        dcc.Dropdown(
            df['region'].unique(),
            "Select Region",
            id="region-selector"
        )
    ]),
    
    dcc.Graph(
        id="sales_graph",
        figure=fig
    )
])

@app.callback(
    Output('sales_graph', 'figure'),
    Input('region-selector', 'intput')
)
def update_graph(region):
    fig = px.line(df[df['region'] == region], x="date", y="sales")
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)