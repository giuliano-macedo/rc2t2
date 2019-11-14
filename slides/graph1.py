import matplotlib.pyplot as plt
import pandas as pd
import pickle


table=pickle.load(open("table.p","rb"))

xs=table["Year"][:-2]

ys1=table["XSS"][:-2]
ys2=table["Sql Injection"][:-2]
ys3=table["Overflow"][:-2]
ys4=table["DoS"][:-2]

data=list(zip(xs,ys1,ys2,ys3,ys4))

df=pd.DataFrame(data,columns=["Ano","XSS","SQL Injection","Buffer Overflow","Negação de serviço"])

df.set_index("Ano").plot()

plt.savefig("no_ataques.pdf",format="pdf",dpi=300)