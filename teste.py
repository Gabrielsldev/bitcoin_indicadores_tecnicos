import pandas as pd
from pandas._testing import assert_frame_equal
import sys


# Carrega os argumentos fornecidos por comando de linha
full_cmd_arguments = sys.argv

# Retira o primeiro argumento (teste.py) e atribui os nomes dos arquivos às variáveis arquivo1 e arquivo2
argument_list = full_cmd_arguments[1:]
arquivo1 = argument_list[0]
arquivo2 = argument_list[1]

# Lê os arquivos e atribui às variáveis df1 e df2 para serem passadas à função assert_frame_equal para que
# possam ser comparadas
df1 = pd.read_csv(arquivo1)
df2 = pd.read_csv(arquivo2)

print(assert_frame_equal(df1, df2))

