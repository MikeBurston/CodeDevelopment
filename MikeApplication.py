import streamlit
import requests
import snowflake.connector
import pandas as pd

streamlit.text('Hello World')

my_cur = snowflake.connector.connect(**streamlit.secrets["snowflake"]).cursor()x
my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
