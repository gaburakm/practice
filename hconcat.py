import altair as alt
import pandas as pd
import argparse

def main():
    parser = argparse.ArgumentParser(description='Create line graphs with points and a 95%\
        bootstrapped confidence interval, and horizontally concatenate them')
    
    parser.add_argument('-i', '--infile', type=argparse.FileType('r'),\
        help='the file with the data you wish to use')
#values of x and y we want to use if we only make 1 graph
    parser.add_argument("-x1","--x1_column", type=str,\
        help="The column you wish to set as X variable")
    parser.add_argument("-y1","--y1_column",  type=str,\
        help="The column you wish to set as Y variable")
    parser.add_argument('-t1', '--treatment1', type=str,\
        default='missing', help='how to seperate data, if needed')
#values of x and y for a 2nd graph    
    parser.add_argument("-x2","--x2_column", type=str,\
        help="The column you wish to set as X variable")
    parser.add_argument("-y2","--y2_column",  type=str,\
        help="The column you wish to set as Y variable")
    parser.add_argument('-t2', '--treatment2', type=str,\
        default ='missing2', help='how to seperate data, if needed')
#values of x and y for a 3rd graph
    parser.add_argument("-x3","--x3_column", type=str,\
        help="The column you wish to set as X variable")
    parser.add_argument("-y3","--y3_column",  type=str,\
        help="The column you wish to set as Y variable")
    parser.add_argument('-t3', '--treatment3', type=str,\
        default='missing3', help='how to seperate data, if needed')

    args = parser.parse_args()
    df = args.infile

    if args.treatment1 != missing
        chart1 = alt.Chart(iris).mark_point().encode(
            x='args.x1_column',
            y='args.y1_column',
        ).properties(
            height=300,
            width=300
        )
        chart = chart1
        else:
            if args.treatment2 != missing2
                chart1 = alt.Chart(df).mark_point().encode(
                    x='args.x1_column',
                    y='args.y1_column',
                ).properties(
                    height=300,
                    width=300
                )
                chart2 = alt.Chart(df).mark_point().encode(
                    x='args.x2_column',
                    y='args.y2_column',
                ).properties(
                    height=300,
                    width=300
                )
                chart = alt.hconcat(chart1, chart2)
            else:
                if args.treatment3 != missing3
                    chart1 = alt.Chart(df).mark_point().encode(
                        x='args.x1_column',
                        y='args.y1_column',
                    ).properties(
                        height=300,
                        width=300
                    )
                    chart2 = alt.Chart(df).mark_point().encode(
                        x='args.x2_column',
                        y='args.y2_column',
                    ).properties(
                        height=300,
                        width=300
                    )
                    chart3 = alt.Chart(df).mark_point().encode(
                        x='args.x3_column',
                        y='args.y3_column',
                    ).properties(
                        height=300,
                        width=300
                    )
                    chart = alt.hconcat(chart1, chart2, chart3)
    return chart