from application import app
from flask import render_template,url_for
import pandas as pd
import json
import plotly
from plotly import *
import plotly.graph_objects as go
import plotly.express as px
import tst1 as yh
import requests
@app.route("/")
def index():
    vr=yh.nik()
    #df=px.data.medals_wide()
    #fig1=px.bar(df,x="nation",y=['gold','silver','bronze'], title='Wide=Form Input')
    fig=go.Figure(go.Pie(name="graph",
                         values=[vr[0],vr[1],vr[2]],
                         labels=["R","py","jav"],
                         text=['nik','shalini','sowmya'],
                         hovertemplate="%{label}: <br>Popularity: %{percent}"))
    graph1JSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template("index.html",graph1JSON=graph1JSON)


