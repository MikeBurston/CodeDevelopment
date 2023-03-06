import streamlit
import requests
import snowflake.connector
import pandas

streamlit.text('Hello World')

cnn = snowflake.connector.connect(
            user='BIGMIKE2023',
            password='Army501a!',
            account='su30921.ca-central-1.aws',
            warehouse='pc_rivery_wh',
            database='pc_rivery_db',
            schema='public'
            )

cs = cnn.cursor()
sql = 'SELECT * FROM FRUIT_LOAD_LIST'
cs.execute(sql)
df = cs.fetch_pandas_all()
cs.close()
cnn.close()

print(df.head(10))
