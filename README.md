# **Documentação Desafio-Smarttbot**

## Desafio Técnico para Desenvolvedor de Estratégias
###### Desenvolvido por **Gabriel Sobreira Lopes**

### Descrição

* A aplicação calcula dois indicadores técnicos financeiros a partir de dados do Bitcoin:
  * **Médias móveis exponenciais**
  * **Bandas de Bollinger**

* O dataset utilizado foi retirado do Kaggle neste [link](https://www.kaggle.com/mczielinski/bitcoin-historical-data/data#coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv).

**NOTA:** No desafio, foi indicado a utilização do arquivo `coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv`. Conforme histórico no Kaggle, ele foi removido na atualização de setembro de 2020, versão 3. Os dados para a formação dos candlesticks ("Open", "High", "Low" e "Close") encontram-se agora no arquivo `bitstampUSD_1-min_data_2012-01-01_to_2020-09-14.csv`, fornecido no mesmo [link](https://www.kaggle.com/mczielinski/bitcoin-historical-data/data#coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv). Dessa forma, **foi utilizado o arquivo** `bitstampUSD_1-min_data_2012-01-01_to_2020-09-14.csv`.

***

### Instrunções de uso

* É necessário fazer o [download](https://www.kaggle.com/mczielinski/bitcoin-historical-data/data#coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv) do arquivo `bitstampUSD_1-min_data_2012-01-01_to_2020-09-14.csv`. O arquivo possui 280Mb, ou seja, ultrapassa os 100Mb permitidos pelo Github e por isso não está no repositório.

* Os pacotes necessários para a execução do programa encontram-se no aquivo [requirements.txt](https://github.com/Gabrielsldev/Desafio-Smarttbot/blob/main/requirements.txt) neste repositório. São eles: 
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

**O programa deve ser executado com parâmetros fornecidos através de argumentos em linha de comando:**

`$ python main.py arg1 arg2`

* A aplicação aceita dois argumentos:
  * **Data de Início**, no formato `AAAA/MM/DD`.
  * **Data de Fim**, no formato `AAAA/MM/DD`.

* É feito um teste para saber se os argumentos estão no formato indicado.

* O banco de dados fornecido possui dados entre as datas 2012/01/01 e 2020/09/14. É feito um teste para saber se os argumentos estão dentro do período indicado.

***

### Resultados esperados

Após a execução do programa, os saídas esperadas são:

**Um arquivo** `.ZIP` **contendo um arquivo** `CSV` **com o seguinte formato:**

|timestamp|indicador-0|indicador-1|indicador-2|indicador-3|indicador-4|
|---------|-----------|-----------|-----------|-----------|-----------|
|data/hora|   .....   |   .....   |   .....   |   .....   |   .....   |
|data/hora|   .....   |   .....   |   .....   |   .....   |   .....   |
|data/hora|   .....   |   .....   |   .....   |   .....   |   .....   |
|data/hora|   .....   |   .....   |   .....   |   .....   |   .....   |

* Cada coluna representa os seguintes indicadores:
  * **indicador-0:** Média Móvel Exponencial de 10 períodos
  * **indicador-1:** Média Móvel Exponencial de 30 períodos
  * **indicador-2:** Banda Superior - Bandas de Bollinger
  * **indicador-3:** Média Móvel Simples - Bandas de Bollinger
  * **indicador-4:** Banda Inferior - Bandas de Bollinger

**Dois arquivos** `PNG` **na pasta** `images` **com os gráficos de candlestick:**
  * Um com o indicador Médias Móveis Exponenciais.
  * Um com o indicador Bandas de Bollinger.

***

### Implementação

Inicialmente, o código foi feito no Jupyter Notebook, por ser uma ferramenta excelente para visualizar e manipular dados de maneira rápida e prática. O arquivo `.ipynp` pode ser encontrado no respositório.

* Foi utilizado a biblioteca `Pandas` para a manipulação dos dados.
  * Limpeza dos dados com a retirada de informações desnecessárias, diminuindo o tamanho do banco de dados e, consequentemente, aumentando a velicidade.
  * Manipulação dos dados utilizando funções para calcular os indicadores necessários.

* Foi utilizado a biblioteca `Plotly` para plotar os gráficos por ser versátil e de fácil uso para gráficos com dados financeiros.
  * Outra ferramenta excelente para plotar gráficos OHLC é o mplfinance, mas o Plotly permite interação no Jupyter Notebook, fato que pesou na escolha.
  * O pacote `Kaleido` é utilizado pelo `Plotly` para exportar os gráficos como `PNG`.

Foi utilizado o PyCharm para a criação do [arquivo](https://github.com/Gabrielsldev/Desafio-Smarttbot/blob/main/main.py) `main.py` que pode ser executado em linha de comando com os argumentos como parâmetros, conforme explicado nas instruções de uso.

* Foi utilizado _regular expressions_ para verificar se or argumentos estão no formato `AAAA/MM/DD` juntamente com _if statements_ para verificar se as datas escolhidas estão dentro do período fornecido pelo banco de dados.


***

### Limitações