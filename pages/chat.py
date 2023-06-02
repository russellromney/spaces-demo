import random
import uuid
from dash import html
import dash_bootstrap_components as dbc
import dash_quill

import data


def make_message(sentence, replies=False):
    person = random.choice(data.people)
    return dict(
        id=uuid.uuid4().hex,
        name=person["name"],
        date="2021-01-01",
        image=person["image"],
        sentence=sentence,
        replies=(make_replies() if replies else []),
    )


def make_replies():
    return [
        make_message(
            "...".join(random.choices(data.replies, k=random.choice([1, 3, 7]))),
            replies=False,
        )
        for reply in data.replies
        if random.random() > 0.98
    ]


def display_message(message, show_replies_button=True):
    return dbc.Row(
        [
            dbc.Col(
                html.Img(
                    src=message["image"], height="50px", style=dict(borderRadius="50%")
                ),
                width=2,
            ),
            dbc.Col(
                [
                    dbc.Stack(
                        [
                            html.Strong(message["name"]),
                            html.I(message["date"]),
                        ],
                        direction="horizontal",
                        gap=3,
                    ),
                    dbc.Row(
                        dbc.Col(message["sentence"]),
                    ),
                    *(
                        [
                            dbc.Button(
                                [
                                    "Thread",
                                    dbc.Badge(
                                        len(message["replies"]),
                                        className="ms-2",
                                        color="primary",
                                    ),
                                ],
                                id={
                                    "type": "replies-button",
                                    "index": message["id"],
                                },
                                color="secondary",
                                size="sm",
                            )
                        ]
                        if show_replies_button and message["replies"]
                        else []
                    ),
                ],
                width=10,
            ),
        ]
    )


def make_tab():
    messages = [make_message(x, replies=True) for x in data.sentences]
    layout = html.Div(
        [
            dbc.ListGroup(
                [dbc.ListGroupItem(display_message(x)) for x in messages],
                flush=True,
                id="chat-list",
            ),
            html.Br(),
            dash_quill.Quill(
                id="chat-input",
                maxLength=2000,
                modules={
                    "toolbar": data.quill_mods,
                    "clipboard": {
                        "matchVisual": False,
                    },
                }
            ),
            dbc.Button("Send Message",color='success',id='send-chat',size='sm',style=dict(minWidth='200px')),
        ],
        style=dict(
            # display="flex",
            # overflow="auto",
            flexDirection="column-reverse",
            # overflow="inherit",
        ),
    )
    return {
        "layout": layout,
        "messages": messages,
    }
