import streamlit
import snowflake.connector
import pandas as pd

streamlit.text('Hello World')

cs = snowflake.connector.connect(**streamlit.secrets["snowflake"])
sql = "Select * From FRUIT_LOAD_LIST"
cs.execute(sql)
df = cs.fetch_pandas_all()
cs.close()
cnn.close()

print(df.head(5))
