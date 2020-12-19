import pandas as pd
import plotly.graph_objects as go
import os
import sys
import getopt

df = pd.read_csv("bitstampUSD_1-min_data_2012-01-01_to_2020-09-14.csv")
df_copy = df.copy()

candlestick_df = df_copy.drop(["Volume_(BTC)", "Volume_(Currency)", "Weighted_Price"], axis=1).dropna()

candlestick_df["Timestamp"] = pd.to_datetime(candlestick_df["Timestamp"], unit='s')
candlestick_df.set_index("Timestamp", inplace=True)

# dia_inicio = "2019/12/31"
# dia_fim = "2020/01/01"

#Command line arguments
full_cmd_arguments = sys.argv
argument_list = full_cmd_arguments[1:]
dia_inicio = argument_list[0]
dia_fim = argument_list[1]


date_time_inicio = pd.to_datetime(dia_inicio)
date_time_fim = pd.to_datetime(dia_fim)

dados_para_teste = candlestick_df[(candlestick_df.index >= date_time_inicio) & (candlestick_df.index <= date_time_fim)]

periodos1 = 10
k10 = (2 / (periodos1 + 1))

periodos2 = 40
k20 = (2 / (periodos2 + 1))

mme10 = dados_para_teste.ewm(alpha=k10, adjust=False).mean()
mme20 = dados_para_teste.ewm(alpha=k20, adjust=False).mean()

dados_candles = {
    'x': dados_para_teste.index,
    'open': dados_para_teste["Open"],
    'close': dados_para_teste["Close"],
    'high': dados_para_teste["High"],
    'low': dados_para_teste["Low"],
    'type': 'candlestick',
    'name': 'BitCoin',
    'showlegend': False
}

dados_mme10 = {
    'x': dados_para_teste.index,
    'y': mme10["Close"],
    'type': 'scatter',
    'mode': 'lines',
    'line': {
        'width': 1,
        'color': 'blue'
            },
    'name': 'MME 10'
}

dados_mme20 = {
    'x': dados_para_teste.index,
    'y': mme20["Close"],
    'type': 'scatter',
    'mode': 'lines',
    'line': {
        'width': 1,
        'color': 'red'
            },
    'name': 'MME 20'
}

dados_grafico = [dados_candles, dados_mme10, dados_mme20]

fig = go.Figure(data=dados_grafico)
fig.update_layout(xaxis_rangeslider_visible=False)

compression_opts = dict(method='zip', archive_name='out.csv')
mme10.to_csv('out.zip', compression=compression_opts)

if not os.path.exists("images"):
    os.mkdir("images")

fig.write_image("images/fig1.png")
