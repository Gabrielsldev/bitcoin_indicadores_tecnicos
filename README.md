# **Documentação Desafio-Smarttbot**

## Desafio Técnico para Desenvolvedor de Estratégias

### Descrição

* A aplicação calcula dois indicadores técnicos financeiros a partir de dados do Bitcoin:
  * **Médias móveis exponenciais**
  * **Bandas de Bollinger**

* O dataset utilizado foi retirado do Kaggle neste [link](https://www.kaggle.com/mczielinski/bitcoin-historical-data/data#coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv).

**NOTA:** No desafio, foi indicado a utilização do arquivo `coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv`. Conforme histórico no Kaggle, ele foi removido na atualização de setembro de 2020, versão 3. Os dados para a formação dos candlesticks ("Open", "High", "Low" e "Close") encontram-se agora no arquivo `bitstampUSD_1-min_data_2012-01-01_to_2020-09-14.csv`, fornecido no mesmo [link](https://www.kaggle.com/mczielinski/bitcoin-historical-data/data#coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv). Dessa forma, **foi utilizado o arquivo** `bitstampUSD_1-min_data_2012-01-01_to_2020-09-14.csv`.

### Instrunções de uso

É necessário fazer o [download](https://www.kaggle.com/mczielinski/bitcoin-historical-data/data#coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv) do arquivo `bitstampUSD_1-min_data_2012-01-01_to_2020-09-14.csv`. O arquivo possui 280Mb, ou seja, ultrapassa os 100Mb permitidos pelo Github e por isso não está no repositório.

Os pacotes necessários para a exeução do programa encontram-se no aquivo [requirements.txt](https://github.com/Gabrielsldev/Desafio-Smarttbot/blob/main/requirements.txt) neste repositório.

O programa deve ser executado com parâmetros fornecidos através de argumentos em linha de comando.






