In the file analysis.py there are:

Variables:
YEAR - the year used in analysis is 2010, but the original file has measurements ranging from 1955 to 2011.
MONTH - second column of the weather_tidy.txt and weather_tidy.csv is the month of the year from 1 to 12.
DAY - from 1 to 30 or 31, but some are skipped, if there were no meaningful measurements taken.
TMAX - highest temperature recorded in a day. 
TMIN - lowest temperature recorded in a day.
PRCP - precipitation - the sum of rain, snow, sleet, or hail that fell to or condensed on the ground in a given day.


The files where the results are saved in a clean and tidy-data compliant form:
'weather_tidy.txt' - only rows with all NaN's were deleted
'weather_tidy.csv' - csv version of the file above
'weather_tidy_2.txt' - if 2 of the TMAX, TMIN, PRCP columns were NaN and the third one was 0, the row was deleted
'weather_tidy_2.txt' - csv version of the file above
The only difference is the format and the files are generated by running the 'analysis.py' file. 