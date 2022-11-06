TIER PROTOCOL AND TIDY DATA - README.md

In the Documents folder aside from this document explaining all the basics, there's also Data_Appendix, which describes the variables used in analysis.py and files from Analysis_Data folder and Final_Paper, which is not existant in this project.
 
In the Original_Data folder contains the initial database that was given to clean. 
File 'weather.txt' contains the measurements of max temperature, minimum temperature and the total liquid water equivalent of presumably all precipitation.
The measurements are from Global Historical Climatology Network in Mexico for one of the weather forecast stations.

There's also Metadata folder inside, to stay compliant with the TIER Protocol recommendations, with a link provided to download the dataset, if needed.

In the Command_Files folder there's all the code responsible for changes of the data, all of it in the analysis.py file.
There are comments in the code to make it clearer. The 'analysis.py' file generates the results to Analysis_Data folder.

In the Analysis_Data folder there's the results of the analysis.py file - Two versions of the fully cleaned and processed data files in both .txt and .csv formats for convenience - better described in the Data_Appendix file.

The software used for this analysis:
- Python 3.9.13 in Visual Stude Code (IDE)
- pandas -Version: 1.4.2

It's advised to use Microsoft Excel or matplotlib module for visualisation, if need be, but because of the lack of good data the visualisation will probably be unsatisfactory, therefore I allowed myself to omit it.

Piotr Suchy 407332, AiBD semestr V, 06 Nov 2022

