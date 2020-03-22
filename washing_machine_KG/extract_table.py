import sys
import camelot
import pandas as pd

input_file=sys.argv[1]
pages=sys.argv[2]
output_file=sys.argv[3]

tables = camelot.read_pdf(input_file, pages = pages )

tables.export(output_file,f='csv')
