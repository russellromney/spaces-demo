import random
from dash import html
import dash_bootstrap_components as dbc

import data


def make_tab():
    table_header = [
        html.Thead(
            html.Tr(
                [
                    html.Th(""),
                    html.Th("Name"),
                    html.Th("Assigned To"),
                    html.Th("Due Date"),
                ]
            )
        )
    ]

    def row(task):
        return html.Tr(
            [
                html.Td(dbc.Checkbox(value=task["completed"])),
                html.Td(
                    dbc.Stack(
                        [html.Strong(task["name"]), task["description"]],
                        direction="vertical",
                        gap=1,
                    )
                ),
                html.Td(
                    dbc.Stack(
                        [
                            html.Img(
                                src=task["assigned_to"]["image"],
                                height="50px",
                                style=dict(borderRadius="50%"),
                            ),
                            task["assigned_to"]["name"],
                        ],
                        direction="horizontal",
                        gap=1,
                    )
                ),
                html.Td(task["due_date"]),
            ]
        )

    tasks = [
        dict(
            completed=random.choice([True, False]),
            name=name,
            description=description,
            assigned_to=random.choice(data.people),
            due_date=random.choice(["", "2023-01-01", "2023-05-01"]),
        )
        for name, description in zip(data.task_names, data.task_descriptions)
    ]
    tasks.sort(key=lambda x: (not x["completed"], x["due_date"]), reverse=True)
    table_body = [html.Tbody([row(x) for x in tasks])]
    return dbc.Table(
        table_header + table_body, bordered=False, striped=True, hover=True
    )
