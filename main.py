import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#Encoding = 'ISO-8859-1' refers to the ISO standard Latin-1 character set and encoding format
data=pd.read_csv("covid.csv")
data.columns=("DateReport","countrycode","country","WHOregion","newcases","cumulativecases","newdeaths","cumulativedeaths")

data['DateReport']= pd.to_datetime(data["DateReport"])
dtat_date=data.groupby("DateReport").sum()
print(dtat_date)

fig1=go.Figure()
fig1.add_trace(go.Scatter(x=dtat_date.index,y=dtat_date['cumulativecases'],fill = 'tonexty',line_color='red'))
fig1.update_layout(title = 'Cumulative Cases Worldwide')
fig1.write_html('FIG.html',auto_open=True)

fig2=go.Figure()
fig2.add_trace(go.Scatter(x=dtat_date.index,y=dtat_date['cumulativedeaths'],fill='tonexty',line_color='green'))
fig2.update_layout(title ="CUMULATIVE DEATH worldwide" )
fig2.write_html('FIG2.html',auto_open=True)