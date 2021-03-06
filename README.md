# **BITCOIN E INDICADORES TÉCNICOS**
## MME, Bandas de Bollinger e Nuvem de Ichimoku
###### Desenvolvido por **Gabriel Sobreira Lopes**

### Descrição

* A aplicação calcula três indicadores técnicos financeiros a partir de dados do Bitcoin:
  * **Médias Móveis Exponenciais**
  * **Bandas de Bollinger**
  * **Nuvem de Ichimoku**

* O dataset utilizado foi retirado do Kaggle neste [link](https://www.kaggle.com/mczielinski/bitcoin-historical-data/data#coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv).

**NOTA:** Os dados para a formação dos candlesticks ("Open", "High", "Low" e "Close") encontram-se no arquivo `bitstampUSD_1-min_data_2012-01-01_to_2020-09-14.csv`, fornecido no mesmo [link](https://www.kaggle.com/mczielinski/bitcoin-historical-data/data#coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv). **O arquivo** `bitstampUSD_1-min_data_2012-01-01_to_2020-09-14.csv` **precisa estar no mesmo diretório que o arquivo** `main.py`.

***

### Instruções de uso

* Clone o repositório utilizando `$ git clone https://github.com/Gabrielsldev/bitcoin_indicadores_tecnicos.git` para o diretório de trabalho desejado.
  * O arquivo `bitstampUSD_1-min_data_2012-01-01_to_2020-09-14.csv` encontra-se no respositório em formato `.zip` no arquivo [archive.zip](https://github.com/Gabrielsldev/bitcoin_indicadores_tecnicos/blob/main/archive.zip).
  * Também é possível fazer o [download](https://www.kaggle.com/mczielinski/bitcoin-historical-data/data#coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv) do arquivo `bitstampUSD_1-min_data_2012-01-01_to_2020-09-14.csv` diretamente do Kaggle.

* Os pacotes necessários para a execução do programa encontram-se no arquivo [requirements.txt](https://github.com/Gabrielsldev/bitcoin_indicadores_tecnicos/blob/main/requirements.txt) neste repositório. São eles: 
`install==1.3.4`
`kaleido==0.1.0`
`numpy==1.19.4`
`pandas==1.1.5`
`plotly==4.14.1`
`python-dateutil==2.8.1`
`pytz==2020.4`
`retrying==1.3.3`
`six==1.15.0`

* O usuário deve criar um ambiente virtual e instalar os pacotes listados acima para que seja possível executar o programa.

**O programa** `main.py` **deve ser executado com parâmetros fornecidos através de argumentos em linha de comando:**

`$ python main.py arg1 arg2`

* A aplicação aceita dois argumentos:
  * **Data de Início**, no formato `AAAA/MM/DD`.
  * **Data de Fim**, no formato `AAAA/MM/DD`.

* É feito um teste para saber se os argumentos estão no formato indicado.

* O banco de dados fornecido possui dados entre as datas 2012/01/01 e 2020/09/14. É feito um teste para saber se os argumentos estão dentro do período indicado.

**NOTA:** O arquivo do banco de dados, `bitstampUSD_1-min_data_2012-01-01_to_2020-09-14.csv`, deve estar na mesma pasta do arquivo `main.py`.

***

### Resultados esperados

Após a execução do programa, as saídas esperadas são:

**Um arquivo** `.ZIP` **contendo um arquivo** `CSV` **com o seguinte formato:**

|timestamp|indicador-0|indicador-1|indicador-2|indicador-3|indicador-4|indicador-5|indicador-6|indicador-7|indicador-8|indicador-9|
|---------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
|data/hora|   .....   |   .....   |   .....   |   .....   |   .....   |   .....   |   .....   |   .....   |   .....   |   .....   |
|data/hora|   .....   |   .....   |   .....   |   .....   |   .....   |   .....   |   .....   |   .....   |   .....   |   .....   |
|data/hora|   .....   |   .....   |   .....   |   .....   |   .....   |   .....   |   .....   |   .....   |   .....   |   .....   |
|data/hora|   .....   |   .....   |   .....   |   .....   |   .....   |   .....   |   .....   |   .....   |   .....   |   .....   |

* As colunas representam os seguintes indicadores:
  * **indicador-0:** Média Móvel Exponencial de 10 períodos
  * **indicador-1:** Média Móvel Exponencial de 30 períodos
  * **indicador-2:** Bandas de Bollinger - Banda Superior 
  * **indicador-3:** Bandas de Bollinger - Média Móvel Simples 
  * **indicador-4:** Bandas de Bollinger - Banda Inferior 
  * **indicador-5:** Ichimoku - Tenkan Sen
  * **indicador-6:** Ichimoku - Kijun Sen
  * **indicador-7:** Ichimoku - Senkou Span A
  * **indicador-8:** Ichimoku - Senkou Span
  * **indicador-9:** Ichimoku - Chikou Span

**Três arquivos** `PNG` **na pasta** `images` **com os gráficos de candlestick:**
  * Um com o indicador Médias Móveis Exponenciais.
  * Um com o indicador Bandas de Bollinger.
  * Um com o indicador Nuvens de Ichimoku.

**Os três gráficos também serão plotados no navegador.**

***

### Implementação

Inicialmente, o código foi feito no Jupyter Notebook, por ser uma ferramenta excelente para visualizar e manipular dados de maneira rápida e prática. O [arquivo](https://github.com/Gabrielsldev/bitcoin_indicadores_tecnicos/blob/main/bitcoin_notebook.ipynb) `.ipynp` pode ser encontrado no repositório.

* Foi utilizada a biblioteca `Pandas` para a manipulação dos dados.
  * Limpeza dos dados com a retirada de informações desnecessárias, diminuindo o tamanho do banco de dados e, consequentemente, aumentando a velocidade.
  * Manipulação dos dados utilizando funções para calcular os indicadores necessários.

* Foi utilizada a biblioteca `Plotly` para plotar os gráficos por ser versátil e de fácil uso para gráficos com dados financeiros.
  * Outra boa ferramenta para plotar gráficos OHLC é o `mplfinance`, mas o `Plotly` permite interação diretamente no navegador e no Jupyter Notebook, fato que pesou na escolha.
  * O pacote `Kaleido` é utilizado pelo `Plotly` para exportar os gráficos como `PNG`.

Foi criado o [arquivo](https://github.com/Gabrielsldev/bitcoin_indicadores_tecnicos/blob/main/main.py) `main.py`, que pode ser executado em linha de comando com os argumentos como parâmetros, conforme explicado nas instruções de uso.

* Foi utilizado _regular expressions_ para verificar se os argumentos estão no formato `AAAA/MM/DD` juntamente com _if statements_ para verificar se as datas escolhidas estão dentro do período fornecido pelo banco de dados.


***

### Testes

O programa `teste.py` pode ser utilizado para fazer testes e comparar dois arquivos `CSV` gerados pelo programa `main.py`.

**O arquivo** `teste.py` **deve ser executado com parâmetros fornecidos através de argumentos em linha de comando:**

`$ python teste.py arg1 arg2`

* Os argumentos devem ser os nomes dos arquivos a serem testados, por exemplo: `$ python teste.py dataset1.csv dataset2.csv`

Os dois arquivos serão transformados em dataframes e comparados. Caso haja divergências, será informado no terminal.
* A saída _None_ significa que não há divergências.

**NOTA:** Os dois arquivos a serem comparados devem estar no mesmo diretório que o programa `teste.py`.

***

### Limitações

A aplicação apresenta algumas limitações:

* O programa aceita como parâmetros somente valores de Dia de Início e Dia de Fim.
  * Nesse ponto, há algumas melhorias que podem ser feitas:
    * O banco de dados possui, na coluna `Timestamp`, informação de data e hora. Uma melhoria pode ser a implementação de argumentos com data e hora para permitir períodos intraday.
    * Permitir, via parâmetros fornecidos através de argumentos em linha de comando, a alteração dos períodos das Médias Móveis Exponenciais, por exemplo, dentre outros indicadores.

* Testes automatizados e mais complexos.
  * O programa `teste.py` permite testar e comparar dois arquivos `CSV` desde que o usuário forneça os parâmetros como argumentos na linha de comando, ou seja, de forma manual. Uma possível melhoria é implementar uma automatização dos testes.

***
