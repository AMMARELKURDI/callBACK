from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import streamlit as st
df = px.data.iris()
app = Dash(__name__)
app.layout = html.Div([html.H4("Interactive scatter plot with Iris dataset"),
        dcc.Graph(id="scatter-plot"),
        html.P("Filter by petal width:"),
        dcc.RangeSlider(
            id="range-slider",
            min=0,
            max=2.5,
            step=0.1,
            marks={0: "0", 2.5: "2.5"},
            value=[0.5, 2])])

@app.callback(
    Output("scatter-plot", "figure"),
    Input("range-slider", "value"),)
def update_chart(slider_range):
    low, high = slider_range
    mask = (df["petal_width"] > low) & (df["petal_width"] < high)
    fig = px.scatter(
        df[mask],
        x="sepal_width",
        y="sepal_length",
        color="species",
        size="petal_length",
        hover_data=["petal_width"])
    return fig

