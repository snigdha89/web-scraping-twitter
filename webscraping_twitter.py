import twint
import nest_asyncio
import pandas as pd 
import matplotlib.pyplot as plt

nest_asyncio.apply()
# Configure
c = twint.Config()
c.Search = "\"Booster shot\"" "Omicron"
c.Store_csv = True
c.Output = "Desktop/Assignment1.csv"
c.Lang = "en"
c.Limit = 300
twint.run.Search(c)

data = pd.read_csv("Desktop/Assignment1.csv")
final = data['tweet'].str.lower()
omicron = []
se = []
booster = []
vaccine = []
for i in range (0,len(final)):
    omicron.append(final[i].count("omicron"))
    se.append(final[i].count("side effect"))
    booster.append(final[i].count("booster"))
    vaccine.append(final[i].count("vaccine"))
s_o = sum(omicron)
s_se = sum(se)
s_b = sum(booster)
s_v = sum(vaccine)
x = ('side effect','omicron' , 'booster', 'vaccine' )
y = (s_se,s_o,s_b, s_v)
plt.bar(x,y,align='center') # A bar chart
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.50)
plt.title('Word Frequency Histogram')
plt.show()
print(final)
