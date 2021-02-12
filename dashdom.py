import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash_table 
from dash.exceptions import PreventUpdate
import flask
from flask import Flask
import pandas as pd
import dateutil.relativedelta
from datetime import date
import datetime
import yfinance as yf
import numpy as np
import praw
import sqlite3
import plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def ticker_inputs(inputID, pickerID, MONTH_CUTTOFF):
    #calculate the current date
    currentDate = date.today()
    #calculate past date for the max allowed date
    pastDate = currentDate -     dateutil.relativedelta.relativedelta(months=MONTH_CUTTOFF)
    
    #return the layout components
    return html.Div([
            dcc.Input(id = inputID, type="text", placeholder="MSFT")
            , html.P(" ")  
            , dcc.DatePickerRange(
            id = pickerID,
            min_date_allowed=pastDate,
            start_date = pastDate,
            #end_date = currentDate
            )])

def make_card(alert_message, color, cardbody, style_dict = None):
    
    return  dbc.Card([  dbc.Alert(alert_message, color=color)
        ,dbc.CardBody(cardbody)
        ], style = style_dict)

def make_item(button, cardbody, i):
    # This function makes the accordion items 
    return dbc.Card([
        dbc.CardHeader(
            html.H2(
                dbc.Button(
                    button,
                    color="link",
                    id=f"group-{i}-toggle"))),
        dbc.Collapse(
            dbc.CardBody(cardbody),
            id=f"collapse-{i}")])

