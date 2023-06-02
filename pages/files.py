import random
import uuid
from dash import dcc, html, ALL, no_update, Input, Output, State, MATCH, ctx
import dash_bootstrap_components as dbc

import data


def make_tab():
    filenames = [
        "_".join(
            random.choices(
                list(
                    set(
                        [
                            y.lower().replace(".", "")
                            for x in data.sentences
                            for y in x.split()
                        ]
                    )
                ),
                k=random.choice(
                    [
                        2,
                        4,
                    ]
                ),
            )
        )
        + random.choice([".pdf", ".txt", ".csv", ".mp4"])
        for _ in range(random.randint(3, 20))
    ]
    files = [
        dict(
            id=uuid.uuid4().hex,
            name=name,
            person=random.choice(data.people),
            date=random.choice(
                ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-05"]
            ),
        )
        for name in filenames
    ]

    table_header = [
        html.Thead(
            html.Tr(
                [
                    html.Th("Name"),
                    html.Th("Person"),
                    html.Th("Date"),
                    html.Th(""),
                ]
            )
        )
    ]

    def row(file):
        return html.Tr(
            [
                html.Td(file["name"]),
                html.Td(
                    dbc.Stack(
                        [
                            html.Img(
                                src=file["person"]["image"],
                                height="50px",
                                style=dict(borderRadius="50%"),
                            ),
                            file["person"]["name"],
                        ],
                        direction="horizontal",
                        gap=1,
                    )
                ),
                html.Td(file["date"]),
                html.Td(
                    dbc.Button(
                        "⬇️",
                        id={
                            "type": "download-file-button",
                            "index": file["id"],
                            "name": file["name"],
                        },
                        color="light",
                        size="sm",
                    )
                ),
            ]
        )

    files.sort(key=lambda x: x["date"], reverse=True)
    table_body = [html.Tbody([row(x) for x in files])]

    return [
        html.Br(),
        dbc.Table(table_header + table_body, bordered=False, striped=True, hover=True),
    ]
