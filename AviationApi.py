import requests
import pandas as pd
from flatten_json import flatten
#import csv

#url='https://api.aviationapi.com/v1/airports'
url='https://api.aviationapi.com/v1/charts'
data={"apt":"KAVL"}

r = requests.get(url,params=data)
a=r.json()
a=a['KAVL'][0]
#print(a)
fl=flatten(a)
print("*********************************")
print(fl)
final=pd.json_normalize(fl)
final.to_csv("aviation.csv")





#print(a.keys())
#print(a['KAVL'][0])
#print(a['KAVL'][0].keys())
#print(a)
#print(a.keys())
#print(message)
#print(status)
#print(status_code)
''' 
# this is manual method
print(a)
header=['state', 'state_full', 'city', 'volume', 'airport_name', 'military', 'faa_ident', 'icao_ident', 'chart_seq', 'chart_code', 'chart_name', 'pdf_name', 'pdf_path']
store_data=[]
#print(a['KAVL'][7])
#print(len(a['KAVL']))
count=0
for x in range(1,len(a['KAVL'])):
    k=a['KAVL'][count]
    li=[k['state'],k['state_full'],k['city'],k['volume'],k['airport_name'],k['military'],k['faa_ident'],k['icao_ident'],k['chart_seq'],k['chart_code'],k['chart_name'],k['pdf_name'],k['pdf_path'],]
    count+=1
    store_data.append(li)
#print(count)
#print(store_data)
with open('aviation.csv','w', encoding='UTF8', newline='') as f:
    writer=csv.writer(f)
    writer.writerow(header)
    writer.writerows(store_data)
'''
print('DONE')