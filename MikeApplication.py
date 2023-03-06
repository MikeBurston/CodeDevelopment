import streamlit
import pandas
import snowflake.connector

streamlit.text('Hello World')

snowflake-connector-python

conn = snowflake.connector.connect(
            user="BIGMIKE2023",
            password="Army501a!",
            account="su30921.ca-central-1.aws",
            warehouse="pc_rivery_wh",
            database="pc_rivery_db",
            schema="public")
