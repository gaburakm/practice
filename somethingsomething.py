import altair as alt
import pandas as pd
import argparse

def main():
  parser = argparse.ArgumentParser(description='Create a line chart with a 95% confidence interval\
    band')

  parser.add_argument('-i', '--infile', type=argparse.FileType('r'),\
    help='the file with the data you wish to use')
  parser.add_argument("-x","--x_column", type=str,\
    help="The column you wish to set as X variable")
  parser.add_argument("-y","--y_column",  type=str,\
    help="The column you wish to set as Y variable")
 
  args = parser.parse_args()
  df = args.infile

  base = alt.Chart(df)
  scatterplot = base.mark_point().encode(
     x='args.x_column',
     y='args.y_column',
  )
  line = base.mark_line().encode(
     x='args.x_column',
     y='args.y_column'
  )
  band = base.mark_errorband(extent='ci').encode(
     x='args.x_column',
     y=alt.Y('args.y_column'),
  )
  band + line + scatterplot

if __name__ == '__main__':
    main()