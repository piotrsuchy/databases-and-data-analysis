import pandas as pd
# import numpy as np

with open("Original_Data/weather.txt", encoding='utf-8') as f:
    line = f.readlines()
    # the new table will consist of 6 columns, described in Data_Appendix.md
    # each row will be a distinct observation:
    table = 'YEAR;MONTH;DAY;TMIN;TMAX;PRCP'+'\n'
    # the original weather.txt has 1713 coimns, therefore the range,
    # the increment is 3, because the TMAX, TMIN AND PRCP had unique rows:
    for i in range(1, 1713, 3):
        # the year that interest us is 2010, so the rest is ommited:
        if line[i][11:15] == '2010':
            for d in range(1, 32):
                q = 0
                new_line = ''
                # if any of the variables' measured value is -9999,
                # that means that measurement either didn't take place
                # or was an error. Therefore, the value of -9999
                # is changed to NaN to better illustrate that:
                tmax = line[i-1][13+8*d:21+8*d]
                if tmax == '-9999   ':
                    tmax = 'NaN'
                    q += 1
                # getting rid of the S sign - which is either a mistake,
                # or an indicator of a type of measurement. Either way,
                # it's not of an interest to us, so we slice the string
                # removing redundant characters.
                if tmax[-1] == 'S':
                    tmax = tmax[:-3]

                # just as 2 comments above, indexing of the line, depends on the day:
                tmin = line[i][13+8*d:21+8*d]
                if tmin == '-9999   ':
                    tmin = 'NaN'
                    q += 1
                # getting rid of the S sign - same way as above with tmax
                if tmin[-1] == 'S':
                    tmin = tmin[:-3]

                # just as 2 comments above, indexing of the line, depends on the day:
                prcp = line[i+1][13+8*d:21+8*d]
                if prcp == '-9999   ':
                    prcp = 'NaN'
                    q += 1
                # getting rid of the S sign - same way as above with tmin:
                if prcp[-1] == 'S':
                    prcp = prcp[:-3]
                # if in a measurement of a day all of
                # tmax, tmin and prcp are NAN - that row is skipped:
                if q == 3:
                    continue

                # 2 separate options:
                # if days are from 1-9 a 0 at the beginning
                # is added to fix the formatting:
                if d < 10:
                    new_line += line[i][11:15]+';'+line[i][15:17] + \
                        ';0'+str(d)+';'+tmax+';'+tmin+';'+prcp
                    new_line += '\n'
                else:
                    new_line += line[i][11:15]+';'+line[i][15:17] + \
                        ';'+str(d)+';'+tmax+';'+tmin+';'+prcp
                    new_line += '\n'
                # the new row is added to the table:
                table += new_line
    w = open('Analysis_Data/weather_tidy.txt', 'wt')
    # and we write the contents of the table to the file 'weather_tidy.txt'
    w.write(table)
    w.close()
    f.close()

# creating a csv file from weather_tidy.txt,
# so visualisation may be clearer for some users:
weather3 = pd.read_csv("Analysis_Data/weather_tidy.txt", delimiter=';')
weather3.to_csv('Analysis_Data/weather_tidy.csv', sep=';')
