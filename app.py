import streamlit as st
import datetime
import requests
import pandas as pd
from streamlit_folium import st_folium
import folium

url = 'https://taxifaretorstenweindl-248422586834.europe-west1.run.app/predict'
today = datetime.date.today()

st.markdown("""
    ## Wanna take a ride?
""")

col1, col2 = st.columns(2)

with col1:
    date = st.date_input(
        "Please tell me the pickup date:", today)

with col2:
    time = st.time_input('Please tell me the pickup time:', datetime.time(8, 00))
    date_time = str(date) + " " + str(time)

col1, col2 = st.columns(2)
with col1:
    passenger_count = st.number_input('# Passengers', value=1)
with col2:
    pass

col1, col2, col3, col4 = st.columns(4)

with col1:
    # pickup_longitude = st.number_input('PICKUP longitude', value=-73.950655)
    # pickup_longitude = st.slider('PICKUP longitude', min_value=-74, max_value=-73, value=-73.950, step=0.001)
    pickup_longitude = st.slider('PICKUP longitude', min_value=-74.15, max_value=-73.79, step=0.000001, value=-73.950)
with col2:
    # pickup_latitude = st.number_input('PICKUP latitude', value=40.783282)
    pickup_latitude = st.slider('PICKUP latitude', min_value=40.58, max_value=40.78, step=0.000001, value=40.783282)
with col3:
    # dropoff_longitude = st.number_input('DROPOFF longitude', value=-73.984365)
    dropoff_longitude = st.slider('DROPOFF longitude', min_value=-74.15, max_value=-73.79, step=0.000001, value=-73.984365)
with col4:
    # dropoff_latitude = st.number_input('DROPOFF latitude', value=40.769802)
    dropoff_latitude = st.slider('DROPOFF latitude', min_value=40.58, max_value=40.78, step=0.000001, value=40.769802)
# passenger_count = st.number_input('Please tell me the number of passengers')

params = {}
params['pickup_datetime'] = date_time
params['pickup_longitude'] = pickup_longitude
params['pickup_latitude'] = pickup_latitude
params['dropoff_longitude'] = dropoff_longitude
params['dropoff_latitude'] = dropoff_latitude
params['passenger_count'] = passenger_count

response = requests.get(url, params=params)
data = response.json()
fare = round(float(data['fare']),2)
# output_text = f"""
#        Your taxi fare will approximately be:
# """
# st.write(output_text)
st.markdown(f"Your taxi fare will approximately be: **{fare} USD**")
# st.markdown(f"")

map_data_dict = {
    'lat': [pickup_latitude, dropoff_latitude],
    'lon': [pickup_longitude, dropoff_longitude]
}
map_data = pd.DataFrame(map_data_dict)

st.map(map_data)

###################

# Erstelle ein folium-Kartenobjekt
m = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

# Füge einen Marker hinzu, um einen Startpunkt zu haben (optional)
folium.Marker(
    [48.8566, 2.3522],
    popup="Paris",
    tooltip="Paris"
).add_to(m)

# Rendere die Karte und erfasse das Klick-Ereignis
output = st_folium(
    m,
    center=[48.8566, 2.3522],
    zoom=12,
    key="new_map",
    feature_group_to_add=None,
    width=700,
    height=500
)

if output:
    last_clicked = output.get('last_clicked')
    if last_clicked:
        lat = last_clicked.get('lat')
        lon = last_clicked.get('lng')
        st.write(f"Koordinaten des letzten Klicks: Latitude={lat}, Longitude={lon}")
