import pandas as pd
import numpy as np

weatherload=pd.read_csv("rdu-weather-history.csv",sep=";")

datee=weatherload["date"]
all_dates=np.array(datee)
mintemps=weatherload["tmin"]
all_mintemps=np.array(mintemps)
maxtemps=weatherload["tmax"]
all_maxtemps=np.array(maxtemps)
rain=weatherload["prcp"]
all_rains=np.array(rain)
snows=weatherload["snow"]
all_snow=np.array(snows)
snowd=weatherload["snwd"]
all_snowd=np.array(snowd)
windsp=weatherload["awnd"]
all_windsp=np.array(windsp)
all_temps=all_mintemps+all_maxtemps

def data_summary():
    #This would give a general summary of the whole file
    totalelements=weatherload.shape
    nrows=totalelements[0]
    ncolumns=totalelements[1]
    daterange1=all_dates[0]
    daterange2=all_dates[-1]
    return (
        f"Data Summary\n"
        f"______________\n"
        f"Number of rows: {nrows}\n"
        f"Number of columns: {ncolumns}\n"
        f"Date range: {daterange1} - {daterange2}\n")
    
def hottest():
    hotday=np.max(all_maxtemps)
    day=np.where(all_maxtemps ==hotday)
    date=all_dates[day]
    return hotday,date
    
def coldest():
    coldday=np.min(all_mintemps)
    day=np.where(all_mintemps ==coldday)
    date=all_dates[day]
    return coldday,date
    
def average_t():
    avg_t=np.mean(all_temps)
    return avg_t
    
def average_w():
    avg_w=weatherload["awnd"]
    avg_wind=avg_w.mean()
    return avg_wind
    
def tempdata():
    all_t=weatherload[["date","tmin","tmax"]]
    sorted_df=all_t.sort_values("tmax")
    sorted_df=sorted_df.reset_index(drop =True)
    return sorted_df
    
def rainy():
    rainydays=weatherload[["date","prcp"]]
    sorted_df=rainydays.sort_values("prcp")
    sorted_df=sorted_df.reset_index(drop= True)
    return sorted
    
def windy():
    windy=weatherload[["date", "awnd"]]
    sorted_df=windy.sort_values("awnd")
    sorted_df=sorted_df.reset_index(drop= True)
    return sorted_df
    
def snowy():
    snows=weatherload[["date","snow"]]
    sorted_df=snows.sort_values("snow")
    sorted_df=sorted_df.reset_index(drop= True)
    return sorted_df
    
def snow_d():
    snowd=weatherload[["date","snwd"]]
    sorted_df=snowd.sort_values("snwd")
    sorted_df=sorted_df.reset_index(drop= True)
    return sorted_df
    
def n_rows():
    num=int(input("Please input only the number of the rows you want to access\n"))
    numrow=weatherload.iloc[0:num]
    return numrow
    
def detection():
    #This would check anomalies for all the data columns:
    #Minimum temperatures 
    mean_tmin=np.mean(all_mintemps)
    std_tmin=np.std(all_mintemps)
    threshold=mean_tmin+2*std_tmin
    anomalies=all_mintemps[all_mintemps >threshold]
    print("Checking for anomalies in minimum temperatures.......")
    if anomalies.size ==0:
        print("No anomalies found")
    else:
        print(f"Anomlies: {anomalies}")
    
    #maximum temperatures 
    mean_tmax=np.mean(all_maxtemps)
    std_tmax=np.mean(all_maxtemps)
    threshold=mean_tmax +2*std_tmax
    anomalies=all_maxtemps[all_maxtemps >threshold]
    print("Checking for anomalies in maximum temperatures.......")
    if anomalies.size ==0:
        print("No anomalies found")
    else:
        print(f"Anomlies: {anomalies}")
        
        #rainfalls
    mean_prcp=np.mean(all_rains)
    std_prcp=np.std(all_rains)
    threshold=mean_prcp +10*std_prcp
    anomalies=all_rains[all_rains>threshold]
    print("Checking for anomalies in precipitations.......")
    if anomalies.size==0:
        print("No anomalies found")
    else:
        print(f"Anomlies: {anomalies}")
        
    #snowfall
    mean_snow=np.mean(all_snow)
    std_snow=np.std(all_snow)
    threshold =mean_snow +10*std_snow
    anomalies=all_snow[all_snow>threshold]
    print("Checking for anomalies in snow......")
    if anomalies.size ==0:
        print("No anomalies found")
    else:
        print(f"Anomlies: {anomalies}")
        
    #snow depths 
    mean_snwd=np.mean(all_snowd)
    std_snwd=np.std(all_snowd)
    threshold=mean_snwd +10*std_snwd
    anomalies=all_snowd[all_snowd> threshold]
    print("Checking for anomalies in snow depths.......")
    if anomalies.size==0:
        print("No anomalies found")
    else:
        print(f"Anomlies: {anomalies}")
        
        #average wind speeds 
    mean_awnd=np.mean(all_windsp)
    std_awnd=np.std(all_windsp)
    threshold =mean_awnd +2*std_awnd
    anomalies=all_windsp[all_windsp >threshold]
    print("Checking for anomalies in wind speed averages.....")
    if anomalies.size==0:
        print("No anomalies found")
    else:
        print(f"Anomlies: {anomalies}")
      