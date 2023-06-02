from dash import Dash
import dash_bootstrap_components as dbc

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.MATERIA],
    external_scripts=[
        "http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"
    ],
)
app.server.secret_key = "secret"
app.title = "Spaces"
