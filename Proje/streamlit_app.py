import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_notebook, show
import plotly.graph_objects as go
import plotly.express as px
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


paths = [r'.\DataSet_Global2000\aroissues-forbes-global-2000-2008-2019\G2000_' + '{0}.xlsx'.format(i) for i in range(8, 23)]
dfs = [pd.read_excel(path).head(200) for path in paths]

df_8, df_9, df_10, df_11, df_12, df_13, df_14, df_15, df_16, df_17, df_18, df_19, df_20, df_21, df_22 = dfs

dfs = [globals()[f"df_{i}"] for i in range(8, 23)]
katergoriler = ['Industry', 'Country']

for df in dfs:
    for kolon in katergoriler:
        df[kolon] = df[kolon].astype('category')


dfs = [globals()[f"df_{i}"] for i in range(8, 23)]

market_values = []
for df in dfs:
    market_values.append(df['Market_Value'].sum())

a = list(range(2008,2023))
mv = [x/1000000 for x in market_values]

fig_genel = go.Figure(
    layout=dict(
        title="Top 200 Toplam Piyasa Değeri",
        
        xaxis_title='sene',
        yaxis_title='trilyon dolar',
    ), 
)

fig_genel.add_trace(go.Scatter(x=a, y=mv, name='piyasa değeri', line=dict(width=3, color='blue')))



#
#
#       ALTTAKİNİ DEĞİŞTİR
#
#




fig_satis_kar_8 = px.scatter(df_8, x='Sales', y='Profits', color='Industry', size='Market_Value', hover_name='Company', title='Bunu değiştir')


df_8_new = df_8[~df_8['Company'].isin(['ExxonMobil', 'Royal Dutch Shell', 'BP', 'Wal-Mart Stores'])]





#
#
#       ALTTAKİNİ DEĞİŞTİR
#
#

fig_satis_kar_8_no_outlier = px.scatter(df_8_new, x='Sales', y='Profits', color='Industry', size='Market_Value', hover_name='Company', title='Bunu değiştir')




countries = ['United States', 'United Kingdom', 'China', 'Japan', 'Germany', 'Canada', 'Switzerland', 'Russia', 'Italy', 'Spain', 'India', 'South Korea']
dfs = [globals()[f"df_{i}"] for i in range(8, 23)]

country_market_values = {country: [df[df['Country'] == country]['Market_Value'].sum()/1000000 for df in dfs] for country in countries}
a = list(range(2008, 2023))

fig_ülkeler = go.Figure(layout=dict(title="Şirketlerin Ülkelere Göre Toplam Piyasa Değeri", xaxis_title='sene', yaxis_title='Trilyon Dolar'))

colors = ['navy', 'maroon', 'yellow', 'pink', 'black', 'red', 'blue', 'grey', 'green', 'olive', 'orange', 'purple']
for i, country in enumerate(countries):
    fig_ülkeler.add_trace(go.Scatter(x=a, y=country_market_values[country], name=country, line=dict(width=3, color=colors[i])))



sektörler = [
    'Banking',
    'Drugs & Biotechnology',
    'Oil & Gas Operations', 
    'Consumer Durables', 
    'Telecommunications services', 
    'Food, Drink & Tobacco',
    'IT Software & Services',
    'Insurance',
    'Retailing',
    'Diversified Financials',
    'Conglomerates',
    'Semiconductors'
]


dfs = [globals()[f"df_{i}"] for i in range(8, 23)]

industry_market_values = {sektor: [df[df['Industry'] == sektor]['Market_Value'].sum()/1000000 for df in dfs] for sektor in sektörler}
a = list(range(2008, 2023))

fig_ülkeler_sectors = go.Figure(layout=dict(title="Şirketlerin Sektörlere Göre Toplam Piyasa Değeri", xaxis_title='sene', yaxis_title='Trilyon Dolar'))

colors = ['navy', 'maroon', 'yellow', 'pink', 'black', 'red', 'blue', 'grey', 'green', 'olive', 'orange', 'purple']
for i, sektor in enumerate(sektörler):
    fig_ülkeler_sectors.add_trace(go.Scatter(x=a, y=industry_market_values[sektor], name=sektor, line=dict(width=3, color=colors[i])))




df_15_cleaned = df_15.drop(columns='Rank_nr').select_dtypes('number')

normalized_df_15 = df_15_cleaned.apply(lambda x: x / x.abs().max(), axis=0)

top200_general_fig = px.histogram(
    normalized_df_15,
    nbins=50,
    marginal="box",
    title="2015 Top 200 Genel Dağılım",
    height=800,
    width=600,
)

top200_general_fig.update_layout(
    # grid=dict(visible=True),
    xaxis=dict(showgrid=True),
    yaxis=dict(showgrid=False),
    legend=dict(x=1, y=1),
    barmode="overlay",
)





df_15_cleaned_2 = df_15.drop(columns='Rank_nr')

sPlot = px.scatter_matrix(df_15_cleaned_2)
sPlot.update_layout(
    showlegend=False,
    width=800,
    height=800,
    title="Pair Plot - 2015 Top 200"
)



st.title("Main Title")

st.plotly_chart(fig_genel)
st.plotly_chart(fig_satis_kar_8)
st.plotly_chart(fig_satis_kar_8_no_outlier)
st.plotly_chart(fig_ülkeler)
st.plotly_chart(fig_ülkeler_sectors)
st.plotly_chart(top200_general_fig)
st.plotly_chart(sPlot)

