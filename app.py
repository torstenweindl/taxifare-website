import streamlit as st
import datetime
import requests
import pandas as pd

url = 'https://taxifaretorstenweindl-248422586834.europe-west1.run.app/predict'

st.markdown("""
    # Wanna take a ride?
""")

col1, col2 = st.columns(2)

with col1:
    date = st.date_input(
        "Please tell me the pickup date:",
        datetime.date(2019, 7, 6))

with col2:
    time = st.time_input('Please tell me the pickup time:', datetime.time(8, 45))
    date_time = str(date) + " " + str(time)

col1, col2, col3, col4 = st.columns(4)

with col1:
    pickup_longitude = st.number_input('PICKUP longitude')
with col2:
    pickup_latitude = st.number_input('PICKUP latitude')
with col3:
    dropoff_longitude = st.number_input('DROPOFF longitude')
with col4:
    dropoff_latitude = st.number_input('DROPOFF latitude')
# passenger_count = st.number_input('Please tell me the number of passengers')

passenger_count = st.slider('# Passengers', 1, 10, 1)

params = {}
params['pickup_datetime'] = date_time
params['pickup_longitude'] = pickup_longitude
params['pickup_latitude'] = pickup_latitude
params['dropoff_longitude'] = dropoff_longitude
params['dropoff_latitude'] = dropoff_latitude
params['passenger_count'] = passenger_count


map_data = pd.DataFrame(pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude)


# just hardcoding temporarily
# params['pickup_datetime'] = '2014-07-06 19:18:00'


response = requests.get(url, params=params)
data = response.json()
# st.write(data)
# st.write(response.status_code)

fare = round(float(data['fare']),2)

output_text = f"""
      Your taxi fare will approximately be:
 """

st.write(output_text)

st.markdown(f"# {fare} USD")
