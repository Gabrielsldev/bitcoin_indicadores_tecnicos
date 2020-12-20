import pandas as pd
from pandas._testing import assert_frame_equal
import sys


#Command line arguments
full_cmd_arguments = sys.argv
argument_list = full_cmd_arguments[1:]
arquivo1 = argument_list[0]
arquivo2 = argument_list[1]

df1 = pd.read_csv(arquivo1)
df2 = pd.read_csv(arquivo2)

print(assert_frame_equal(df1, df2))

