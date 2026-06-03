import os
import pandas as pd
import analysis

while True:
    filepath = input(
        "Enter weather file path: "
    ).strip()

    if os.path.exists(filepath):
        break

    print("File not found. Try again.")

weatherload = pd.read_csv(
    filepath,
    sep=";")
required = [
    "date",
    "tmax",
    "tmin",
    "prcp",
    "awnd",
    "snow",
    "snwd"]

for col in required:
    if col not in weatherload.columns:
        print(f"Missing column: {col}")
        break
print('Welcome to Chrys Weather Data Analyzer')

try:
    while True:
        options=int(input("Please select an option by choosing the number associated with the option\n1. Dataset Summary\n2. Hottest Day\n3. Coldest Day\n4. Average Temperature\n5. Average Wind Speed\n6. View Temperature Data\n7. Rainy Days\n8. Windy Days\n9. Snow Days\n10. Snow Depth Analysis\n11. View first 'n' rows of file\n12. Detect Anomalies\n13. Exit\n"))
    
        if options == 1:
            print(analysis.data_summary())
        
        if options == 2:
            hotday,date=analysis.hottest()
            print(f"The hottest day was {hotday} and was recorded on {date}\n")
        
        if options == 3:
            coldday,date=analysis.coldest()
            print(f"The hottest day was {coldday} and was recorded on {date}\n")
        
        if options == 4:
            avg_t=analysis.average_t()
            print(f"The average temp is: {avg_t}\n")
        
        if options == 5:
            avg_wind=analysis.average_w()
            print(f"The average wind speed is: {avg_wind}\n")
        
        if options == 6:
            sorted_df=analysis.tempdata()
            print(f"Please note that these have been sorted in a ascending order of maximum temperatures..\n{sorted_df}\n")
        
        if options == 7:
            sorted=analysis.rainy()
            print(f"Please note that these have been sorted in a ascending order of precipitations.\n{sorted_df}\n")
        
        if options == 8:
            sorted=analysis.windy()
            print(f"Please note that these have been sorted in a ascending order of average wind speeds.\n{sorted_df}\n")
        
        if options == 9:
            sorted=analysis.snowy()
            print(f"Please note that these have been sorted in a ascending order of snowfall\n{sorted_df}\n")
        
        if options == 10:
            sorted=analysis.snow_d()
            print(f"Please note that these have been  sorted in a ascending order of snowfall depths.\n{sorted_df}\n")
        
        if options == 11:
            numrow=analysis.n_rows()
            print(numrow)
        
        if options == 12:
            analysis.detection()
            print("All done.\n")
        
        if options==13:
            break
except ValueError:
    print("Sorry something went wrong..:(")