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



#Section4
streamlit.stop()

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

my_cur.execute("Select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text("Contains")
#streamlit.text(my_data_rows)
streamlit.dataframe(my_data_rows)

my_fruits=my_data_rows
streamlit.multiselect("Pick some fruits:", list(my_fruits))
