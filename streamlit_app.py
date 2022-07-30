import requests
import streamlit
import pandas
#python uit requirements.txt
import snowflake.connector
from urllib.error import URLError

streamlit.title('nonsense nonsense')
streamlit.header('import pandas Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

streamlit.header("Fruityvice Fruit Advice!")

Try:
  fruit_choice=streamlit.text_input('What Fruit?','Kiwi')
if not fruitchoice: 
  streamlit.write('the user answered',fruit_choice)
else:
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
  # streamlit.text(fruityvice_response.json())

  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  # write your own comment - what does this do?
  streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  streamlit.error()
  
  
 
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

#streamlit.stop()

my_fruits=my_data_rows
streamlit.multiselect("Pick some fruits:", list(my_fruits))
