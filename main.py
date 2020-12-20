import pandas as pd
import plotly.graph_objects as go
import os
import sys
import re

#ACEITA OS
full_cmd_arguments = sys.argv
argument_list = full_cmd_arguments[1:]
dia_inicio = argument_list[0]
dia_fim = argument_list[1]

teste_formato = re.compile("^[0-9]{4}[/][0-9]{2}[/][0-9]{2}$")

if teste_formato.match(dia_inicio and dia_fim):
    datetime_inicio = pd.to_datetime(dia_inicio)
    datetime_fim = pd.to_datetime(dia_fim)
else:
    print("Erro: Os parâmetros devem seguir o formato AAAA/MM/DD.")
    exit()

data_maxima = pd.to_datetime("2020/09/14")
data_minima = pd.to_datetime("2012/01/01")

if datetime_inicio < data_minima or datetime_fim > data_maxima:
    print("Erro: Datas devem estar entre 2012/01/01 e 2020/09/14.")
    exit()
elif datetime_inicio > datetime_fim:
    print("Erro: Data inicial deve ser menor do que data final.")
    exit()


# CARREGA O BANCO DE DADOS

# Carrega o banco de dados e exlcui os dados desnecessários
df = pd.read_csv("bitstampUSD_1-min_data_2012-01-01_to_2020-09-14.csv")
df_copy = df.copy()
candlestick_df = df_copy.drop(["Volume_(BTC)", "Volume_(Currency)", "Weighted_Price"], axis=1).dropna()
candlestick_df["Timestamp"] = pd.to_datetime(candlestick_df["Timestamp"], unit='s')
candlestick_df.set_index("Timestamp", inplace=True)

## DEFINE O PERÍODO

# Período definido pelo usuário via argumentos de linha de comando

datetime_fim = datetime_fim + pd.DateOffset(1)

dados_selecionados = candlestick_df[(candlestick_df.index >= datetime_inicio) &
                                  (candlestick_df.index <= datetime_fim)]

## MÉDIAS MÓVEIS EXPONENCIAIS

# Cálculo do atenuado K
periodos10 = 10
k10 = (2 / (periodos10 + 1))
periodos30 = 30
k30 = (2 / (periodos30 + 1))

# Cálculo das médias móveis exponenciais utilizando o método ewm com a função mean()
mme10 = dados_selecionados["Close"].ewm(alpha=k10, adjust=False).mean()
mme30 = dados_selecionados["Close"].ewm(alpha=k30, adjust=False).mean()


## PLOTAR GRÁFICO

# Dicionários que servirão de parâmetros para plotar o gráfico das médias móveis exponenciais.

candles_grafico = {
    "x": dados_selecionados.index,
    "open": dados_selecionados["Open"],
    "close": dados_selecionados["Close"],
    "high": dados_selecionados["High"],
    "low": dados_selecionados["Low"],
    "type": 'candlestick',
    "name": 'BitCoin',
    "showlegend": True
}

mme10_grafico = {
    "x": dados_selecionados.index,
    "y": mme10,
    "type": 'scatter',
    "mode": 'lines',
    "line": {
        "width": 1,
        "color": 'blue'
            },
    "name": 'MME 10'
}

mme30_grafico = {
    "x": dados_selecionados.index,
    "y": mme30,
    "type": 'scatter',
    "mode": 'lines',
    "line": {
        "width": 1,
        "color": 'red'
            },
    "name": 'MME 20'
}

dados_grafico = [candles_grafico, mme10_grafico, mme30_grafico]

fig = go.Figure(data = dados_grafico)
fig.update_layout(xaxis_rangeslider_visible=False)

fig.show()

## CRIAR PNG - MÉDIA MÓVEL EXPONENCIAL

if not os.path.exists("images"):
    os.mkdir("images")

fig.write_image("images/mme.png", width=3840, height=2160)

## BANDAS DE BOLLINGER

# Gera os dados para as Bandas de Bollinger utilizando o período definido pelo usuário
# via argumentos de linha de comando.

desvio_padrao = dados_selecionados["Close"].rolling(window=20, min_periods=1).std()

banda_mms = dados_selecionados["Close"].rolling(window=20, min_periods=1).mean()
banda_superior = banda_mms + (desvio_padrao * 2)
banda_inferior = banda_mms - (desvio_padrao * 2)

# Dicionários que servirão de parâmetros para plotar o gráfico das Bandas de Bollinger.

candles_grafico = {
    "x": dados_selecionados.index,
    "open": dados_selecionados["Open"],
    "close": dados_selecionados["Close"],
    "high": dados_selecionados["High"],
    "low": dados_selecionados["Low"],
    "type": 'candlestick',
    "name": 'BitCoin',
    "showlegend": True
}

banda_mms_grafico = {
    "x": banda_mms.index,
    "y": banda_mms,
    "type": 'scatter',
    "mode": 'lines',
    "line": {
        "width": 1,
        "color": 'red'
            },
    "name": 'MÉDIA MÓVEL SIMPLES'
}

banda_superior_grafico = {
    "x": banda_superior.index,
    "y": banda_superior,
    "type": 'scatter',
    "mode": 'lines',
    "line": {
        "width": 1,
        "color": 'black'
            },
    "name": 'BANDA SUPERIOR'
}

banda_inferior_grafico = {
    "x": banda_inferior.index,
    "y": banda_inferior,
    "type": 'scatter',
    "mode": 'lines',
    "fill": 'tonexty',
    "line": {
        "width": 1,
        "color": 'gray'
            },
    "name": 'BANDA INFERIOR'
}


dados_grafico = [candles_grafico, banda_mms_grafico, banda_superior_grafico, banda_inferior_grafico]

fig = go.Figure(data = dados_grafico)
fig.update_layout(xaxis_rangeslider_visible=False)

fig.show()

## CRIAR PNG - BANDAS DE BOLLINGER

if not os.path.exists("images"):
    os.mkdir("images")

fig.write_image("images/bollinger.png", width=3840, height=2160)

## NUVEM DE ICHIMOKU

# Tenkan-sen (linha de conversão)
tenkan_sen_max = dados_selecionados["High"].rolling(window=9).max()
tenkan_sen_min = dados_selecionados["Low"].rolling(window=9).min()
tenkan_sen = (tenkan_sen_max + tenkan_sen_min)*0.5

# Kijun-sen (linha de base)
kijun_sen_max = dados_selecionados["High"].rolling(window=26).max()
kijun_sen_min = dados_selecionados["Low"].rolling(window=26).min()
kijun_sen = (kijun_sen_max + kijun_sen_min)*0.5

# Senkou Span A (período líder A)
senkou_span_a = ((tenkan_sen + kijun_sen)*0.5).shift(26)

# Senkou Span B (período líder B)
senkou_span_b_max = dados_selecionados["High"].rolling(window=52).max()
senkou_span_b_min = dados_selecionados["Low"].rolling(window=52).min()
senkou_span_b = ((senkou_span_b_max + senkou_span_b_min)*0.5).shift(26)

# Chikou Span (período de atraso)
chikou_span = dados_selecionados["Close"].shift(-26)

# Dicionários que servirão de parâmetros para plotar o gráfico da Nuvem de Ichimoku.

candles_grafico = {
    "x": dados_selecionados.index,
    "open": dados_selecionados["Open"],
    "close": dados_selecionados["Close"],
    "high": dados_selecionados["High"],
    "low": dados_selecionados["Low"],
    "type": 'candlestick',
    "name": 'BitCoin',
    "showlegend": True
}

tenkan_sen_grafico = {
    "x": tenkan_sen.index,
    "y": tenkan_sen,
    "type": 'scatter',
    "mode": 'lines',
    "line": {
        "width": 1,
        "color": 'blue'
            },
    "name": 'TENKAN SEN'
}

kijun_sen_grafico = {
    "x": kijun_sen.index,
    "y": kijun_sen,
    "type": 'scatter',
    "mode": 'lines',
    "line": {
        "width": 1,
        "color": 'red'
            },
    "name": 'KIJUN_SEN'
}

senkou_span_a_grafico = {
    "x": senkou_span_a.index,
    "y": senkou_span_a,
    "type": 'scatter',
    "mode": 'lines',
    "line": {
        "width": 1,
        "color": 'black'
            },
    "name": 'SENKOU SPAN A'
}

senkou_span_b_grafico = {
    "x": senkou_span_b.index,
    "y": senkou_span_b,
    "type": 'scatter',
    "mode": 'lines',
    "fill": 'tonexty',
    "line": {
        "width": 1,
        "color": 'gray'
            },
    "name": 'SENKOU SPAN B'
}

chikou_span_grafico = {
    "x": chikou_span.index,
    "y": chikou_span,
    "type": 'scatter',
    "mode": 'lines',
    "line": {
        "width": 1,
        "color": 'gray'
            },
    "name": 'CHIKOU SPAN'
}


dados_grafico = [candles_grafico, tenkan_sen_grafico, kijun_sen_grafico,
                 senkou_span_a_grafico, senkou_span_b_grafico, chikou_span_grafico]

fig = go.Figure(data = dados_grafico)
fig.update_layout(xaxis_rangeslider_visible=False)

fig.show()

## CRIAR ARQUIVO PNG PARA NUVEM DE ICHIMOKU

if not os.path.exists("images"):
    os.mkdir("images")

fig.write_image("images/ichimoku.png", width=3840, height=2160)

## CRIAR O ARQUIVO CSV

# Cria um dataframe com os dados solicitados no desafio.

arquivo_saida = pd.DataFrame(data=[dados_selecionados.index, mme10, mme30,
                                   banda_superior, banda_mms, banda_inferior,
                                   tenkan_sen, kijun_sen, senkou_span_a, senkou_span_b, chikou_span]).T

column_names = ["timestamp", "indicador-0", "indicador-1", "indicador-2", "indicador-3", "indicador-4",
               "indicador-5", "indicador-6", "indicador-7", "indicador-8", "indicador-9"]

# COLUNAS:
# timestamp = Timestamp
# indicador-0 = Média Móvel 10 Períodos
# indicador-1 = Média Móvel 30 Períodos
# indicador-2 = Bollinger - Banda Superior
# indicador-3 = Bollinger - MMS
# indicador-4 = Bollinger - Banda Inferior
# indicador-5 = Ichimoku - Tenkan Sen
# indicador-6 = Ichimoku - Kijun Sen
# indicador-7 = Ichimoku - Senkou Span A
# indicador-8 = Ichimoku - Senkou Span
# indicador-9 = Ichimoku - Chikou Span

# Altera os nomes das colunas de acordo com a lista column_names e organiza os dados para a saída CSV.

for i in arquivo_saida.columns:
    arquivo_saida[column_names[i]] = arquivo_saida[i]

arquivo_saida.set_index("timestamp", inplace=True)

arquivo_saida = arquivo_saida.drop([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], axis=1)

compression_opts = dict(method="zip", archive_name="indicadores.csv")
arquivo_saida.to_csv("out.zip", compression=compression_opts)
