import streamlit as st
import datetime
import requests

url = 'https://taxifaretorstenweindl-248422586834.europe-west1.run.app/predict'

st.markdown("""
    # Wanna take a ride?
""")

date = st.date_input(
    "Please tell me the pickup date:",
    datetime.date(2019, 7, 6))

time = st.time_input('Please tell me the pickup time:', datetime.time(8, 45))

date_time = str(date) + " " + str(time)

pickup_longitude = st.number_input('Please insert PICKUP longitude')
pickup_latitude = st.number_input('Please insert PICKUP latitude')
dropoff_longitude = st.number_input('Please insert DROPOFF longitude')
dropoff_latitude = st.number_input('Please insert DROPOFF latitude')
# passenger_count = st.number_input('Please tell me the number of passengers')

passenger_count = st.slider('Select number of passengers', 1, 10, 1)

params = {}
params['pickup_datetime'] = date_time
params['pickup_longitude'] = pickup_longitude
params['pickup_latitude'] = pickup_latitude
params['dropoff_longitude'] = dropoff_longitude
params['dropoff_latitude'] = dropoff_latitude
params['pickup_longitude'] = pickup_longitude
params['passenger_count'] = passenger_count


# just hardcoding temporarily
# params['pickup_datetime'] = '2014-07-06 19:18:00'


response = requests.get(url, params=params)
data = response.json()
# st.write(data)
# st.write(response.status_code)

st.write(int(data['fare']))

# fare = ROUND(float(data['fare']),0)

# output_text = f"""
  #      Your taxi fare will approximately be {fare} USD.
   # """

# st.write(output_text)
