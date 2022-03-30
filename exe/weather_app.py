from tkinter import *
import requests
import json

root = Tk()
root.title('weather app')
root.geometry("380x100")


# http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=556B5ECC-D0ED-460A-A061-937121CD0C44
# structure of data output
"""
[
{"DateObserved":"2020-06-22 ","HourObserved":4,"LocalTimeZone":"PST","ReportingArea":"Las Vegas","StateCode":"NV",
"Latitude":36.206,"Longitude":-115.223,"ParameterName":"O3","AQI":46,"Category":{"Number":1,"Name":"Good"}},
{"DateObserved":"2020-06-22 ","HourObserved":4,"LocalTimeZone":"PST","ReportingArea":"Las Vegas","StateCode":"NV",
"Latitude":36.206,"Longitude":-115.223,"ParameterName":"PM2.5","AQI":30,"Category":{"Number":1,"Name":"Good"}},
{"DateObserved":"2020-06-22 ","HourObserved":4,"LocalTimeZone":"PST","ReportingArea":"Las Vegas","StateCode":"NV",
"Latitude":36.206,"Longitude":-115.223,"ParameterName":"PM10","AQI":31,"Category":{"Number":1,"Name":"Good"}}
]"""


# create zipcode lookup function
def zip_lookup():
    # zip.get()
    # zip_label = Label(root, text=zip.get())
    # zip_label.grid(row=1, column=0, columnspan=2)

    try:
        api_request = requests.get(
            "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=556B5ECC-D0ED-460A-A061-937121CD0C44")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_color = "#00e400"
        elif category == "Moderate":
            weather_color = "#ffff00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#ff7e00"
        elif category == "Unhealthy":
            weather_color = "#ff0000"
        elif category == "Very Unhealthy":
            weather_color = "#8f3f97"
        elif category == "Hazardous":
            weather_color = "#7e0023"
        else:
            weather_color = "white"

        root.configure(bg=weather_color)
        my_label = Label(root, text=city + ", Air Quality: " + str(quality) + ", " + category, font=("Helvetica", 20),
                         bg=weather_color, pady=20)

        my_label.grid(row=2, column=0, columnspan=2)
    except Exception as e:
        print("ERROR....")


zip = Entry(root)
zip.grid(row=0, column=0)

zip_btn = Button(root, text="Lookup zipcode", command=zip_lookup)
zip_btn.grid(row=0, column=1)


root.mainloop()
