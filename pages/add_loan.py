import dash_html_components as html
import dash_core_components as dcc

layout = html.Div([
    html.P("Loan Amount?"),
    dcc.Input(id="loan_amount",
              type="number",
              debounce=True,
              placeholder=0,
              step=100
              ),
    html.Br(),

    html.P("Paid"),
    dcc.Input(id="paid_amount",
              type="number",
              debounce=True,
              placeholder=0
              ),
    html.Br(),
    html.P("Monthly Payments"),
    dcc.Input(id="monthly_payments",
              type="number",
              debounce=True,
              placeholder=100,
              step=10
              ),
    html.Br(),

    html.Button(id="submit_loan_data", type='Submit', children="Submit")
    ])
