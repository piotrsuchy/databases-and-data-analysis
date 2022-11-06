import pandas as pd
import math

with open("Original_Data/weather.txt", encoding='utf-8') as f:
    line = f.readlines()
    # the new table will consist of 6 columns, described in Data_Appendix.md
    # each row will be a distinct observation:
    table = 'YEAR;MONTH;DAY;TMAX;TMIN;PRCP'+'\n'
    # the original weather.txt has 1713 coimns, therefore the range,
    # the increment is 3, because the TMAX, TMIN AND PRCP had unique rows:
    for i in range(1, 1713, 3):
        # the year that interest us is 2010, so the rest is ommited:
        if line[i][11:15] == '2010':
            for d in range(1, 32):
                q = 0
                new_line = ''
                tmax = line[i-1][13+8*d:21+8*d]
                # getting rid of the S sign - which is either a mistake,
                # or an indicator of a type of measurement. Either way,
                # it's not of an interest to us, so we slice the string
                # removing redundant characters.
                if tmax[-1] == 'S':
                    tmax = tmax[:-3]
                # if any of the variables' measured value is -9999 or 0
                # that means that measurement either didn't take place
                # or was an error. Therefore, the value of -9999
                # is changed to NaN to better illustrate that:
                if tmax == '-9999   ' or tmax == '    0':
                    tmax = 'NaN'
                    q += 1
                # getting rid of the S sign - which is either a mistake,
                # or an indicator of a type of measurement. Either way,
                # it's not of an interest to us, so we slice the string
                # removing redundant characters.

                tmin = line[i][13+8*d:21+8*d]
                # getting rid of the S sign - same way as above with tmax
                if tmin[-1] == 'S':
                    tmin = tmin[:-3]
                # just as 2 comments above, indexing of the line, depends on the day:
                if tmin == '-9999   ' or tmin == '    0':
                    tmin = 'NaN'
                    q += 1
                    
                prcp = line[i+1][13+8*d:21+8*d]
                # getting rid of the S sign - same way as above with tmin:
                if prcp[-1] == 'S':
                    prcp = prcp[:-3]
                # just as 2 comments above, indexing of the line, depends on the day:
                if prcp == '-9999   ':
                    prcp = 'NaN'
                    q += 1
                
                if prcp == '    0':
                    prcp = '0'
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
weather_tidy = pd.read_csv("Analysis_Data/weather_tidy.txt", delimiter=';')
weather_tidy.to_csv('Analysis_Data/weather_tidy.csv', sep=';')

def isNaN(x):
    return x != x

# EVERYTHING ANALOGOUSLY TO THE CODE BEFORE, JUST SKIPPING ROWS WITH NAN NAN 0, 
# TO CREATE A CLEARER TABLE WHERE AT LEAST ONE MEASUREMENT HAS TO BE DIFFERENT 
# THAN 0 TO BE AN OBSERVATION:

# better described in Data_Appendix
with open("Original_Data/weather.txt", encoding='utf-8') as f:
    line = f.readlines()
    table_2 = 'YEAR;MONTH;DAY;TMAX;TMIN;PRCP'+'\n'
    for i in range(1, 1713, 3):
        if line[i][11:15] == '2010':
            for d in range(1, 32):
                q = 0
                new_line = ''
                tmax = line[i-1][13+8*d:21+8*d]
                if tmax[-1] == 'S':
                    tmax = tmax[:-3]
                if tmax == '-9999   ' or tmax == '    0':
                    tmax = 'NaN'
                    q += 1
                
                tmin = line[i][13+8*d:21+8*d]
                if tmin[-1] == 'S':
                    tmin = tmin[:-3]
                if tmin == '-9999   ' or tmin == '    0':
                    tmin = 'NaN'
                    q += 1
                    
                prcp = line[i+1][13+8*d:21+8*d]
                if prcp[-1] == 'S':
                    prcp = prcp[:-3]
                if prcp == '-9999   ':
                    prcp = 'NaN'
                    q += 1
                
                if prcp == '    0':
                    prcp = '0'
                    q += 13
                    
                if q == 3 or q == 15 or (q == 2 and tmax == '0'):
                    continue

                if d < 10:
                    new_line += line[i][11:15]+';'+line[i][15:17] + \
                        ';0'+str(d)+';'+tmax+';'+tmin+';'+prcp
                    new_line += '\n'
                else:
                    new_line += line[i][11:15]+';'+line[i][15:17] + \
                        ';'+str(d)+';'+tmax+';'+tmin+';'+prcp
                    new_line += '\n'

                table_2 += new_line
    w = open('Analysis_Data/weather_tidy_2.txt', 'wt')
    w.write(table_2)
    w.close()
    f.close()
    
weather_tidy_2 = pd.read_csv("Analysis_Data/weather_tidy_2.txt", delimiter=';')
weather_tidy_2.to_csv('Analysis_Data/weather_tidy_2.csv', sep=';')
