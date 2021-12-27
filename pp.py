import pandas as pd
class cl_ascii:
  def read_ascii(self,lista):
    l=[]
    i=0
    df=pd.DataFrame(lista, columns=['alpha'])
    while(ord(df.loc[i,'alpha'])!=ord('H') and ord(df.loc[i,'alpha'])!=ord('h')):
      l.append(ord(df.loc[i,'alpha'])*10)
      i=i+1
    if i<len(df['alpha'])-1:
      for i in range(i,len(df['alpha'])):
        l.append(0)
    return l