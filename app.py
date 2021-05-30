from sqlalchemy import create_engine
from dash import Dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from pages import index, add_loan

meta_tags=[
    {'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}
]
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], meta_tags=meta_tags)
app.config.suppress_callback_exceptions =True

engine = create_engine("postgresql://jay:prenda@localhost:5432/money_db")
conn = engine.connect()


app.layout = html.Div([
    dcc.Location(id='url', refresh=False), # what's refresh arg for?
    #navbar,
    dbc.Container(id='page-content', className='mt-4'), # This className='mt-4' is a bootstrap thing to add in
    dcc.Store(id='session', storage_type='session'),
    ])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/add-loan':
        return add_loan.layout
    
    return index.layout


@app.callback(Output('session', 'data'),
              [Input('submit_loan_data', 'click')],
              [State('loan_amount', 'loan'),
               State('paid_amount', 'paid'),
               State('monthly_payments', 'payments')])
def add_new_loan(data, loan, paid, payments):

    if not data:
        data = {"loans": []}

    data['loans'].append({
        "Borrowed": loan,
        "Paid": paid,
        "Money Left": loan - paid,
        "Monthly Payments": payments,
        "Time Left": (loan - paid) / payments
    })
    ## the data for the table needs to be updated with this new data
    ### for now, into an object
    ### later insert into db
    ## return the layout with the table
    return json.dumps(data)


@app.callback(Output('debts', 'children'),
              [Input('session', 'data')])
def update_table_data(data):
    if not data:
        return {"loans": []}
    return data 


if __name__ == "__main__":
    app.run_server(debug=True)
