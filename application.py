from dash import html, dcc, Dash, Input, Output, State, ALL, ctx, no_update, MATCH
import dash_bootstrap_components as dbc
import dash_quill
import flask

from app import app
import data
from pages import chat, spaces

section_style = {"maxHeight": "70vh", "overflow": "auto"}
section_style_short = {"maxHeight": "60vh", "overflow": "auto"}

app.layout = html.Div(
    [
        dbc.NavbarSimple(
            brand="Demo Spaces",
            brand_href="#",
            color="secondary",
            dark=False,
        ),
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                # html.H1("Demo Spaces"),
                                *[
                                    dbc.Row(
                                        dbc.Col(
                                            html.Div(
                                                [
                                                    dbc.Button(
                                                        space,
                                                        color="primary"
                                                        if i == 0
                                                        else "secondary",
                                                        id={
                                                            "type": "space-button",
                                                            "index": space,
                                                        },
                                                        className="d-grid gap-2",
                                                        style=dict(
                                                            width="100%",
                                                            marginTop="10px",
                                                        ),
                                                    ),
                                                ],
                                                style=section_style,
                                            )
                                        ),
                                    )
                                    for i, space in enumerate(data.spaces)
                                ],
                            ],
                            width=2,
                        ),
                        #
                        #
                        dcc.Download(id="download-file"),
                        html.Div(id="scroll-trigger", style=dict(display="none")),
                        dbc.Col(
                            [
                                html.H3(
                                    id="current-space", style=dict(marginTop="10px")
                                ),
                                dbc.Tabs(
                                    [
                                        dbc.Tab(
                                            html.Div(
                                                id="chat-tab", style=section_style
                                            ),
                                            label="Chat 📩",
                                            tab_style={"margin": "auto"},
                                        ),
                                        dbc.Tab(
                                            html.Div(
                                                [
                                                    dcc.Upload(
                                                        id="upload-data",
                                                        children=html.Div(
                                                            [
                                                                "Drag and Drop or ",
                                                                html.A("Select Files"),
                                                            ]
                                                        ),
                                                        style={
                                                            # "width": "100%",
                                                            "height": "60px",
                                                            "lineHeight": "60px",
                                                            "borderWidth": "1px",
                                                            "borderStyle": "dashed",
                                                            "borderRadius": "5px",
                                                            "textAlign": "center",
                                                            "margin": "10px",
                                                        },
                                                        # Allow multiple files to be uploaded
                                                        multiple=True,
                                                    ),
                                                    html.Div(id="output-data-upload"),
                                                    html.Div(
                                                        id="files-tab",
                                                        style=section_style_short,
                                                    ),
                                                ]
                                            ),
                                            label="Files 🗄️",
                                            tab_style={"margin": "auto"},
                                        ),
                                        dbc.Tab(
                                            html.Div(
                                                id="tasks-tab", style=section_style
                                            ),
                                            label="Tasks ✅",
                                            tab_style={"margin": "auto"},
                                        ),
                                    ],
                                ),
                            ],
                            id="tabs-col",
                            width=10,
                        ),
                        #
                        #
                        dbc.Col(
                            [
                                # html.H1("Thread"),
                                html.Br(),
                                html.Div(
                                    dbc.Button(
                                        "Hide Thread",
                                        id="hide-thread-button",
                                        color="secondary",
                                        size="sm",
                                        style=dict(width="100%"),
                                    ),
                                    id="hide-thread-button-parent",
                                    style=dict(display="none"),
                                ),
                                html.Br(),
                                html.Div(id="thread-content", style=section_style),
                            ],
                            id="thread-col",
                            width=4,
                        ),
                    ],
                )
            ],
            style=dict(maxHeight="100vh"),
        ),
    ]
)


@app.callback(
    Output("chat-tab", "children"),
    Output("files-tab", "children"),
    Output("tasks-tab", "children"),
    Output("current-space", "children"),
    Input({"type": "space-button", "index": ALL}, "n_clicks"),
)
def space_content(values):
    space = data.spaces[0]
    if any(values):
        space = ctx.triggered_id["index"]
    return (
        spaces.spaces[space]["chat"]["layout"],
        spaces.spaces[space]["files"],
        spaces.spaces[space]["tasks"],
        space,
    )


@app.callback(
    *[
        Output({"type": "space-button", "index": space}, "disabled")
        for space in data.spaces
    ],
    *[
        Output({"type": "space-button", "index": space}, "color")
        for space in data.spaces
    ],
    Input("current-space", "children"),
    prevent_initial_call=True,
)
def space_button_color_disabled(space):
    return [
        # disabled
        *[False if x != space else True for x in data.spaces],
        # color
        *["secondary" if x != space else "primary" for x in data.spaces],
    ]


# anytime a replies button is clicked, load the thread into the threads container
@app.callback(
    Output("thread-content", "children"),
    Output("hide-thread-button-parent", "style"),
    Output("tabs-col", "width"),
    Output("thread-col", "width"),
    Input("hide-thread-button", "n_clicks"),
    Input({"type": "replies-button", "index": ALL}, "n_clicks"),
    State("current-space", "children"),
    prevent_initial_call=True,
)
def thread_content(clear, populate, space):
    if ctx.triggered_id == "hide-thread-button":
        if clear:
            return "", dict(display="none"), 10, no_update

    if space != flask.session.get("space"):
        flask.session["space"] = space
        return "", dict(display="none"), 10, no_update

    if any(populate):
        message = [
            x
            for x in spaces.spaces[space]["chat"]["messages"]
            if x["id"] == ctx.triggered_id["index"]
        ][0]
        return (
            [
                chat.display_message(message, False),
                html.Hr(),
                dbc.ListGroup(
                    [
                        dbc.ListGroupItem(chat.display_message(x))
                        for x in message["replies"]
                    ],
                    flush=True,
                ),
                html.Br(),
                dash_quill.Quill(
                    id="thread-input",
                    maxLength=2000,
                    modules={
                        "toolbar": data.quill_mods,
                        "clipboard": {
                            "matchVisual": False,
                        },
                    },
                ),
                dbc.Button("Send Reply",color='success',id='send-chat',size='sm',style=dict(minWidth='150px'))
            ],
            dict(),
            6,
            4,
        )
    return no_update, no_update, no_update, no_update


@app.callback(
    Output("download-file", "data"),
    Input({"type": "download-file-button", "index": ALL, "name": ALL}, "n_clicks"),
    prevent_initial_call=True,
)
def download_file(values):
    if any(values):
        return dict(content="Hello world!", filename=ctx.triggered_id["name"])
    return no_update


if __name__ == "__main__":
    app.run_server(
        debug=True,
        port="8000",
    )
