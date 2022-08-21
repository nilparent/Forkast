from matplotlib.pyplot import hist
import pandas as pd
import requests
import csv

url = "https://visual-crossing-weather.p.rapidapi.com/history"
headers = {
    "X-RapidAPI-Key": "ee378a2a33msh48cdc6439c87d2bp137f14jsn055b8a547637",
    "X-RapidAPI-Host": "visual-crossing-weather.p.rapidapi.com"
}

start_date = "2022-06-03"
end_date = "2022-07-03"
location='Paris, France'

def import_historical_weather_data(start_time, end_time, location):
    querystring = {
        "startDateTime": start_time,
        "aggregateHours": "24",
        "location": location,
        "endDateTime": end_time,
        "unitGroup": "metric",
        "dayStartTime": "8:00:00",
        "contentType": "csv",
        "dayEndTime": "17:00:00",
        "shortColumnNames": "0",
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    cr = csv.reader(response.content.decode("utf-8").splitlines(), delimiter=",")
    my_list = list(cr)
    return my_list


historical_weather = []

mean(historical_weather)

for i in range(2, 7):
    start_date = start_date[:6] + str(i-1) + "-07"
    end_date = end_date[:6] + str(i) + "-06"

    print(start_date, end_date)

    weather_data=import_historical_weather_data(str(start_date)[:10]+"T00:00:00",str(end_date)[:10]+"T00:00:00",location)
    print(weather_data)
    weather_data=pd.DataFrame(weather_data[1:],columns=weather_data[0])
    weather_data['Date time']= pd.to_datetime(weather_data['Date time'])
    weather_data['Temperature']= weather_data['Temperature'].astype(float)
    weather_data['Minimum Temperature']= weather_data['Minimum Temperature'].astype(float)
    weather_data['Maximum Temperature']= weather_data['Maximum Temperature'].astype(float)
    weather_data['Precipitation']= weather_data['Precipitation'].astype(float)
    weather_data['Cloud Cover']= weather_data['Cloud Cover'].astype(float)
    weather_data['Relative Humidity']= weather_data['Relative Humidity'].astype(float)
    weather_data['Dew Point']= weather_data['Dew Point'].astype(float)

    historical_weather.append(weather_data)
    print(historical_weather)

for i in range(10, 13):
    if i == 10 :
        start_date = "2021-0" + str(i-1) + "-07"
        end_date = "2021-" + str(i) + "-06"
    else : 
        start_date = "2021-" + str(i-1) + "-07"
        end_date = "2021-" + str(i) + "-06"

    print(start_date, end_date)

    weather_data=import_historical_weather_data(str(start_date)[:10]+"T00:00:00",str(end_date)[:10]+"T00:00:00",location)
    print(weather_data)
    weather_data=pd.DataFrame(weather_data[1:],columns=weather_data[0])
    weather_data['Date time']= pd.to_datetime(weather_data['Date time'])
    weather_data['Temperature']= weather_data['Temperature'].astype(float)
    weather_data['Minimum Temperature']= weather_data['Minimum Temperature'].astype(float)
    weather_data['Maximum Temperature']= weather_data['Maximum Temperature'].astype(float)
    weather_data['Precipitation']= weather_data['Precipitation'].astype(float)
    weather_data['Cloud Cover']= weather_data['Cloud Cover'].astype(float)
    weather_data['Relative Humidity']= weather_data['Relative Humidity'].astype(float)
    weather_data['Dew Point']= weather_data['Dew Point'].astype(float)

    historical_weather.append(weather_data)
    print(historical_weather)

for i in range(2, 9):
    start_date = "2021-0" + str(i-1) + "-07"
    end_date = "2021-0" + str(i) + "-06"

    print(start_date, end_date)

    weather_data=import_historical_weather_data(str(start_date)[:10]+"T00:00:00",str(end_date)[:10]+"T00:00:00",location)
    print(weather_data)
    weather_data=pd.DataFrame(weather_data[1:],columns=weather_data[0])
    weather_data['Date time']= pd.to_datetime(weather_data['Date time'])
    weather_data['Temperature']= weather_data['Temperature'].astype(float)
    weather_data['Minimum Temperature']= weather_data['Minimum Temperature'].astype(float)
    weather_data['Maximum Temperature']= weather_data['Maximum Temperature'].astype(float)
    weather_data['Precipitation']= weather_data['Precipitation'].astype(float)
    try :
        weather_data['Cloud Cover']= weather_data['Cloud Cover'].astype(float)
    except :
        pass
    weather_data['Relative Humidity']= weather_data['Relative Humidity'].astype(float)
    weather_data['Dew Point']= weather_data['Dew Point'].astype(float)

    historical_weather.append(weather_data)
    print(historical_weather)


pd.DataFrame(historical_weather).to_csv("historical_weather_copy.csv")


"""
import csv

header = ['name', 'area', 'country_code2', 'country_code3']
data = [
    ['Albania', 28748, 'AL', 'ALB'],
    ['Algeria', 2381741, 'DZ', 'DZA'],
    ['American Samoa', 199, 'AS', 'ASM'],
    ['Andorra', 468, 'AD', 'AND'],
    ['Angola', 1246700, 'AO', 'AGO']
]

with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)
"""