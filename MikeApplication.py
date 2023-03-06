import streamlit
import pandas
import snowflake.connector

streamlit.text('Hello World')

conn = snowflake.connector.connect(
  user='BIGMIKE2023'
  password='Army501a'
  account='su30921.ca-central-1.aws'
  warehouse='pc_rivery_wh'
  schema='public'
  )

cs = conn.cursor()
sql = "Select * From FRUIT_LOAD_LIST"
cs.execute(sql)
df = cs.fetch_pandas_all()
cs.close()
cnn.close()

print(df.head(5))
