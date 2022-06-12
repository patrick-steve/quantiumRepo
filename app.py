from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('formatted_data.csv')
df = df.sort_values(by='date')

fig = px.line(df, x="date", y="sales", color="region")

app.layout = html.Div(children=[
    html.H1("Sales Price Graph", id="header", style={"backgroundColor": "#161A1D", "color": "#2178BC", "textAlign": 'center'}),
    
    html.Div([
        dcc.Dropdown(
            df['region'].unique(),
            "Select Region",
            id="region-selector"
        )
    ], style={"backgroundColor": "#161A1D"}),
    
    dcc.Graph(
        id="sales_graph",
        figure=fig
    )
])

@app.callback(
    Output('sales_graph', 'figure'),
    Input('region-selector', 'value')
)
def update_graph(region):
    fig = px.line(df[df['region'] == region], x="date", y="sales")
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)