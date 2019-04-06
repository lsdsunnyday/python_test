import numpy as np
import pandas as pd
import bisect
import math

hs13 = pd.read_excel('0406hs_6pol.xlsx','2013')
hs14 = pd.read_excel('0406hs_6pol.xlsx','2014')
grd  = pd.read_excel('0406hs_6pol.xlsx','level')
iaq = grd.IAQI.to_list()

def lsd(col,ikind):
    col = col.to_list()
    ikind = ikind.to_list()
    
    newcol = []
    for i in range(len(col)):
        if math.isnan(col[i]):
            newcol.append(np.nan)
        else:
            index = bisect.bisect(ikind,col[i])
            if index < 8:
                #print(index,i,col[i])
                iaq_h = iaq[index]
                iaq_l = iaq[index-1]

                bp_h = ikind[index]
                bp_l = ikind[index-1]

                newcol.append((iaq_h-iaq_l)/(bp_h-bp_l)*(col[i]-bp_l)+iaq_l)
            else:
                newcol.append(iaq[-1])
    return newcol

vars = [ 'SO2','NO2', 'PM10', 'CO','O3', 'PM2_5'  ]
a = [ '{}_newlist'.format(var) for var in vars ]
print(a)

for ivar in range(len(vars)):
    varname = vars[ivar]
    a[ivar] = lsd(hs14[varname],grd[varname])


data=pd.DataFrame(a,index=[ 'SO2','NO2', 'PM10', 'CO','O3', 'PM2_5']).T 
print((data.head().max(axis=1)))

data['max_value']=data.max(axis=1)
data['max_index'] = np.argmax(data.values,axis=1)
data.to_csv('AQI统计.csv', index=True, sep=',')