import streamlit
import requests
import snowflake.connector
import pandas as pd

streamlit.text('Hello World')

cnn = snowflake.connector.connect(
    user = "BIGMIKE2023",
    password = "Army501a!",
    account = "su30921.ca-central-1.aws",
    warehouse = "pc_rivery_wh",
    database = "pc_rivery_db",
    schema = "public",
    role = "pc_rivery_role"
    )

cs = cnn.cursor()
sql = 'Select * From FRUIT_LOAD_LIST'
cs.execute(sql)
df = cs.fetch_pandas_all()
