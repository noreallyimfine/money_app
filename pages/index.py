import dash_html_components as html
import dash_core_components as dcc
from dash_table import DataTable

debt_cols = ["Borrowed", "Paid", "Money Left", "Time Left", "Monthly Payments"]

layout = html.Div([
    html.H1(children="Our Money App", className="page-header"),
    html.Div([
        dcc.Link(html.Button("Add loan", id='loan-button'), href='/add-loan'),
        DataTable(id='debts',
                  columns=[{"name": i, "id": i} for i in debt_cols],
                  data=[])
    ]),
    ])
