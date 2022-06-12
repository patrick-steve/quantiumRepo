from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('data/output.csv')

fig = px.line(df, x="date", y="sales", color="region")

app.layout = html.Div(children=[
    html.H1(children="Sales Price"),
    dcc.Graph(
        id="sales_graph",
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)