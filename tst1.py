from application import app
from flask import render_template,url_for
import pandas as pd
import json
import plotly
from plotly import *
import plotly.graph_objects as go
import plotly.express as px
import requests
def nik():
    li=[]
    q = requests.get('http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=json')
    tu = q.json()
    v1=tu['dataseries'][0]['cloudcover']
    v2=tu['dataseries'][0]['seeing']
    v3=tu['dataseries'][0]['timepoint']
    li.append(v1)
    li.append(v2)
    li.append(v3)
    return li
