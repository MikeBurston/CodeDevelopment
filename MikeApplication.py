import streamlit
import snowflake.connector
import pandas as pd

streamlit.text('Hello World')

cs = snowflake.connector.connect(**streamlit.secrets["snowflake"])
