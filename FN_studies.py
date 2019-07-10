import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#   Data from : https://cdsp.sciences-po.fr/fr/le-cdsp/resultats-electoraux/

years = ['1965', '1969', '1974', '1981', '1988', '1995', '2002', '2007', '2012', '2017']
partis = [["FN", "EXD", "RN"], ["PC", "LO"], ["PS"], ["EM!"]] # list the parti abreviation in here
rateParties = []

for parti in partis:
    rate = []
    for yr in years:
        filePath = 'PRESIDENTIELLES_1965-2012-csv/cdsp_presi'+yr+'t1_circ.csv'
        print(filePath)

        df = pd.read_csv(filePath)
        total_score = 0
        
        for subPt in parti:
            FNcol = 0
            found = False
            for lbl in df.columns.values:
                if lbl.find(subPt) != -1:
                    found = True
                    break
                FNcol += 1

            FNr = 0
            if found:
                dfSum = df.sum()
                votant = dfSum[5]
                FN = dfSum[FNcol]
                FNr = FN/votant*100.0
            total_score+=FNr
        rate.append(total_score)
    rateParties.append(rate)

# 2017's results : https://www.lemonde.fr/data/france/presidentielle-2017/
# years.append('2017')
# FNrate.append(21.30) 

#   Precise results
print(rateParties)

#   Display the graph
i = 0
for ptr in rateParties:
    st = ""
    for sbpt in partis[i]:
        st += sbpt + " "
    plt.plot(years, ptr, label = st)
    i += 1
plt.title("Presidential elections")
plt.ylabel("%")
plt.legend()
plt.show()
