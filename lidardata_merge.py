import os
import pandas as pd
import numpy as np
import glob

path=r'E:\2017'
file=glob.glob(os.path.join(path, "depol*.txt"))
print(file)

db=[]
for f in file:
 db.append(pd.read_csv(f,sep='\s+',header=None,index_col=0))
df=pd.concat(db)

hgt=np.arange(30,12030,30)
hgt.reshape(1,400)
df.columns=hgt

lidar=df.drop_duplicates()
result.sort_index(level=0)
result.to_csv(r'E:\lidar_dust.csv', index=True, sep=',')