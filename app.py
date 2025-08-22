import streamlit as st
import datetime
import requests
import pandas as pd
from streamlit_folium import st_folium
import folium

url = 'https://taxifaretorstenweindl-248422586834.europe-west1.run.app/predict'
today = datetime.date.today()

st.markdown("""
    ### Wanna take a ride?
""")

col1, col2, col3 = st.columns(3)

with col1:
    date = st.date_input(
        "Pickup date:", today)

with col2:
    time = st.time_input('Pickup time:', datetime.time(8, 00))
    date_time = str(date) + " " + str(time)

with col3:
    passenger_count = st.number_input('# Passengers', value=1)

# col1, col2, col3, col4 = st.columns(4)

# with col1:
    # pickup_longitude = st.number_input('PICKUP longitude', value=-73.950655)
    # pickup_longitude = st.slider('PICKUP longitude', min_value=-74, max_value=-73, value=-73.950, step=0.001)
    # pickup_longitude = st.slider('PICKUP longitude', min_value=-74.15, max_value=-73.79, step=0.000001, value=-73.950)
# with col2:
    # pickup_latitude = st.number_input('PICKUP latitude', value=40.783282)
    # pickup_latitude = st.slider('PICKUP latitude', min_value=40.58, max_value=40.78, step=0.000001, value=40.783282)
# with col3:
    # dropoff_longitude = st.number_input('DROPOFF longitude', value=-73.984365)
    # dropoff_longitude = st.slider('DROPOFF longitude', min_value=-74.15, max_value=-73.79, step=0.000001, value=-73.984365)
# with col4:
    # dropoff_latitude = st.number_input('DROPOFF latitude', value=40.769802)
    # dropoff_latitude = st.slider('DROPOFF latitude', min_value=40.58, max_value=40.78, step=0.000001, value=40.769802)
# passenger_count = st.number_input('Please tell me the number of passengers')



# map_data_dict = {
#     'lat': [pickup_latitude, dropoff_latitude],
#     'lon': [pickup_longitude, dropoff_longitude]
# }
# map_data = pd.DataFrame(map_data_dict)
#
# st.map(map_data)

###################

# 1. Initialisieren des Session State
if 'point_a' not in st.session_state:
    st.session_state.point_a = None
if 'point_b' not in st.session_state:
    st.session_state.point_b = None

# Erstelle ein folium-Kartenobjekt
m = folium.Map(location=[40.783282, -73.950], zoom_start=12)

if st.session_state.point_a:
    folium.Marker(
        [st.session_state.point_a['lat'], st.session_state.point_a['lng']],
        popup="Point A",
        tooltip="Point A",
        icon=folium.Icon(color="green")
    ).add_to(m)

if st.session_state.point_b:
    folium.Marker(
        [st.session_state.point_b['lat'], st.session_state.point_b['lng']],
        popup="Point B",
        tooltip="Point B",
        icon=folium.Icon(color="blue")
    ).add_to(m)

output = st_folium(
    m,
    center=[40.783282, -73.950],
    zoom=13,
    key="multi_click_map",
    width=700,
    height=400
)

if output and 'last_clicked' in output:
    last_clicked = output['last_clicked']
    if last_clicked:
        if not st.session_state.point_a:
            st.session_state.point_a = last_clicked
            st.warning("Point A set. Please select point B.")
            st.rerun() # Führt das Skript erneut aus, um den neuen Zustand zu reflektieren
        elif not st.session_state.point_b:
            st.session_state.point_b = last_clicked
            st.success("Point B set. Prediction is being generated.")
            st.rerun()
        else:
            # Dritter und weitere Klicks: Starte den Zyklus neu
            st.session_state.point_a = last_clicked
            st.session_state.point_b = None
            # st.info("Beide Punkte wurden zurückgesetzt. Bitte wählen Sie jetzt Punkt B aus.")
            st.rerun()


if st.session_state.point_a and st.session_state.point_b:
    params = {}
    params['pickup_datetime'] = date_time
    params['pickup_longitude'] = st.session_state.point_a['lng']
    params['pickup_latitude'] = st.session_state.point_a['lat']
    params['dropoff_longitude'] = st.session_state.point_b['lng']
    params['dropoff_latitude'] = st.session_state.point_b['lat']
    params['passenger_count'] = passenger_count
    response = requests.get(url, params=params)
    data = response.json()
    fare = round(float(data['fare']),2)
    # output_text = f"""
    #        Your taxi fare will approximately be:
    # """
    # st.write(output_text)
    st.markdown(f"Your taxi fare will approximately be:
                ### **USD {fare}**", unsafe_allow_html=True)

    # st.markdown(f"")
