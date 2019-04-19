import pandas as pd
import altair as alt
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
  parser.add_argument('-t', '--treatment', type=str,\
    default='plate', help='how do you want to separate the data. Can use egg_sack_id, well_id, and plate')

  args = parser.parse_args()
  df = args.infile

  base = alt.Chart(args.infile)
  if args.treatment != None:
    scatterplot = alt.Chart(df).mark_point().encode(
     x='args.x_column',
     y='args.y_column',
     color='args.treatment'
   ).properties(
     width=160,
     height=160
    ).facet(
      column='args.treatment'
   )
    line = base.mark_line().encode(
      x='args.x_column',
      y='mean(args.y_column)'
   )
    confidence_interval = base.mark_area(opacity=0.3).encode(
      x='args.x_column',
      y=alt.Y('ci0(args.y_column', title='args.y_column'),
      y2='ci1(args.y_column)'
     )

    confidence_interval + scatterplot + line
    chart.save('chart.png')
  else :
    scatterplot = alt.Chart(df).mark_point().encode(
     x='args.x_column',
     y='args.y_column',
   ).properties(
     width=160,
     height=160
   )
    line = base.mark_line().encode(
      x='args.x_column',
      y='mean(args.y_column)'
   )
    confidence_interval = base.mark_area(opacity=0.3).encode(
      x='args.x_column',
      y=alt.Y('ci0(args.y_column', title='args.y_column'),
      y2='ci1(args.y_column)'
     )

    confidence_interval + scatterplot + line
    chart.save('chart.png')

if __name__ == '__main__':
    main()