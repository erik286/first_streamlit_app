import requests
import streamlit
import pandas
from urllib.error import URLError

streamlit.title('My Moms healthy dinner')
streamlit.header('Breakfast  favorites')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

#Section2
#streamlit.stop()

streamlit.title('Your own fruit smoothy')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

#Section3
#streamlit.stop()

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice=streamlit.text_input('What Fruit?')
  if not fruit_choice: 
    streamlit.error('What fruit do you want information about')
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    # streamlit.text(fruityvice_response.json())

    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    # write your own comment - what does this do?
    streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  streamlit.error()



#Section4
#streamlit.stop()

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

my_cur.execute("Select fruit_name from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text("Contains")
streamlit.text(my_data_rows[1])
streamlit.dataframe(my_data_rows)
pandas.normalize(my_data_rows)

my_fruits=pandas.normalize(my_data_rows)
streamlit.multiselect("Pick some fruits:", list(my_fruits))
