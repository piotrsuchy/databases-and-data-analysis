In the file '10_POMORSKIE.csv' there are 5 variables aside from the index column.

The variables are:
- Dni od zakupu - contains amount of days from the time of purchase
- Marka - brand of the item
- Wiek kupującego - age of the buyer in int
- Płeć kupującego - sex(gender) of the buyer values are: K - female, M - male, bd. - no data
- Ocena - Grade given by the buyer

There are 5 files created for each of the variables:
dni.csv - in bins, how many days have passed 
marka.csv - how many purchases of different brands, grouped by brands
oceny.csv - how many of each grade, grouped by grades
plec.csv - how many of each gender, grouped by gender (with an additional no data label)
wiek.csv - how many customers of certain age, grouped by ranges of ages

I've created 5 separate graphs (bar charts) for each of the variables.
Wykres_Ocen.png contains information about an amount of each grades given by the customers.
Wykres_plec.png contains information about how many purchases were made by each gender.
Wykres_wieku.png contains information about how many customers are in given age ranges.
Wykres_marka.png contains information about how many purchases of different brands there were.
Wykres_dni.png contains information about how many days have passed since purchase - in bins assigned in analysis.py

All the plots are located in the Analysis_Data folder.
