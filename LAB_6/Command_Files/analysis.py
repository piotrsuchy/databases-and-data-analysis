import pandas as pd
# import numpy as np
import matplotlib as plt

# resizing all figures:
plt.rcParams.update({'figure.autolayout': True})

# do zmiany dla kogoś kto chciałby zreprodukować (tylko path_to_change, reszta tak samo):
path_to_change =  "/Users/piotrsuchy/Desktop/AGH/SEMESTR 5/Analiza i Bazy Danych/AiBD/LAB_6"
path_analysis_data = path_to_change + "/Analysis_Data"
path_original_data = path_to_change + "/Original_Data/10_POMORSKIE.csv"

# loading original data in .csv format:
df = pd.read_csv(path_original_data, index_col=0)
df.index.name = "ID"

# Wykres ocen wystawionych przez klientów:
df_ocena = df.filter(['Ocena'], axis = 1)
df_ocena = df_ocena.groupby('Ocena').size()
#df_ocena.columns = ['Ocena', 'Ilość']
df_ocena1 = df_ocena.to_frame()
df_ocena1.columns = ['Ilość']
df_ocena1.to_csv(path_analysis_data + "/oceny.csv") 
plot_ocen = df_ocena1.plot.bar(title = 'Ilość każdej z ocen', legend = 0,rot = 0)
plot_ocen.set_xlabel("Ocena")
plot_ocen.set_ylabel("Ilość")
fig = plot_ocen.get_figure()
fig.savefig(path_analysis_data + "/Wykres_ocen.png")
# print(df_ocena1)

# dataframe z ilością klientów różnych płci i wykres:
df_plec = df.filter(['Płeć kupującego'], axis = 1)
df_plec = df_plec.groupby('Płeć kupującego').size()
df_plec = df_plec.to_frame()
df_plec.columns = ['Ilość']
df_plec.to_csv(path_analysis_data + "/plec.csv")
plot_plec = df_plec.plot.bar(title = 'Ilość klientów danej płci', legend = 0,rot = 0)
plot_plec.set_xlabel("Płeć")
plot_plec.set_ylabel("Ilość klientów danej płci")
fig = plot_plec.get_figure()
fig.savefig(path_analysis_data + "/Wykres_plec.png")

# Dataframe z wiekiem klientów i wykres wieku klientów w danych przedziałach: 
df_wiek = df.filter(['Wiek kupującego'], axis = 1)
df_wiek['Przedział wieku'] = pd.cut(df_wiek['Wiek kupującego'], [0, 25, 35, 45, 60, float('inf')], labels=['<=25', '26-35', '36-45', '46-60', '<=61'])
df_wiek1 = df_wiek['Przedział wieku'].to_frame()
df_wiek2 = df_wiek1.groupby('Przedział wieku').size()
df_wiek2.columns = ['Ilość w przedziale']
df_wiek2.to_csv(path_analysis_data + "/wiek.csv")
plot_wieku = df_wiek2.plot.bar(title = "Ilość klientów w danym przedziale wiekowym")
fig = plot_wieku.get_figure()
fig.autofmt_xdate(rotation=45)
fig.savefig(path_analysis_data + "/Wykres_wiek.png")

# dataframe z markami kupionych przedmiotów i wykres danych marek:
df_marka = df.filter(['Marka'], axis = 1)
df_marka = df_marka.groupby('Marka').size()
df_marka = df_marka.to_frame()
df_marka.columns = ['Ilość']
df_marka.to_csv(path_analysis_data + "/marka.csv")
plot_marka = df_marka.plot.bar(title = 'Ilość zakupionych przedmiotów danej marki', legend = 0,rot = 0)
plot_marka.set_xlabel("Marka")
plot_marka.set_ylabel("Ilość")
fig = plot_marka.get_figure()
fig.savefig(path_analysis_data + "/Wykres_marka.png")

# dataframe z dniami od zakupu i wykres:
df_dni = df.filter(['Dni od zakupu'], axis = 1)
df_dni['Przedział dni'] = pd.cut(df_dni['Dni od zakupu'], [0, 3, 7, 14, 30, float('inf')], labels=['<=3', '4-7', '8-14', '15-30', '<30'])
df_dni1 = df_dni['Przedział dni'].to_frame()
df_dni1 = df_dni1.groupby('Przedział dni').size()
df_dni1.columns = ['Ilość w przedziale']
df_dni1.to_csv(path_analysis_data + "/dni.csv")
plot_dni = df_dni1.plot.bar(title = "Wykres dni od zakupu w danych przedziałach")
plot_dni.set_xlabel("Ile dni minęło od zakupu")
plot_dni.set_ylabel("Ilość")
fig = plot_dni.get_figure()
fig.savefig(path_analysis_data + "/Wykres_dni.png")