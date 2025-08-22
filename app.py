import streamlit as st
import datetime
import requests
import pandas as pd

url = 'https://taxifaretorstenweindl-248422586834.europe-west1.run.app/predict'
today = datetime.date.today()

st.markdown("""
    # Wanna take a ride?
""")

col1, col2 = st.columns(2)

with col1:
    date = st.date_input(
        "Please tell me the pickup date:", today)

with col2:
    time = st.time_input('Please tell me the pickup time:', datetime.time(8, 00))
    date_time = str(date) + " " + str(time)

col1, col2, col3, col4 = st.columns(4)

with col1:
    pickup_longitude = st.number_input('PICKUP longitude', value=-73.950655)
with col2:
    pickup_latitude = st.number_input('PICKUP latitude', value=40.783282)
with col3:
    dropoff_longitude = st.number_input('DROPOFF longitude', value=-73.984365)
with col4:
    dropoff_latitude = st.number_input('DROPOFF latitude', value=40.769802)
# passenger_count = st.number_input('Please tell me the number of passengers')

passenger_count = st.slider('# Passengers', 1, 10, 1)

params = {}
params['pickup_datetime'] = date_time
params['pickup_longitude'] = pickup_longitude
params['pickup_latitude'] = pickup_latitude
params['dropoff_longitude'] = dropoff_longitude
params['dropoff_latitude'] = dropoff_latitude
params['passenger_count'] = passenger_count


map_data_dict = {
    'lat': [pickup_latitude, dropoff_latitude],
    'lon': [pickup_longitude, dropoff_longitude]
}
map_data = pd.DataFrame(map_data_dict)

st.map(map_data)


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
