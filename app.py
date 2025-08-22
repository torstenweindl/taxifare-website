import streamlit as st
import datetime

date = st.date_input(
    "Please tell me the pickup date:",
    datetime.date(2019, 7, 6))

time = st.time_input('Please tell me the pickup time:', datetime.time(8, 45))

pickup_longitude = st.number_input('Please insert PICKUP longitude')
pickup_latitude = st.number_input('Please insert PICKUP latitude')
dropoff_longitude = st.number_input('Please insert DROPOFF longitude')
dropoff_latitude = st.number_input('Please insert DROPOFF latitude')
passenger_count = st.number_input('Please tell me the number of passengers')


st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifaretorstenweindl-248422586834.europe-west1.run.app/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
