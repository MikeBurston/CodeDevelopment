import snowflake.connector as sf
import requests
import pandas as pd

ctx = sf.connect(
    user='BIGMIKE2023',
    password = 'Army501a!',
    account = 'su30921.ca-central-1.aws',
    warehouse = 'compute_wh',
    database = 'SNOWFLAKE_SAMPLE_DATA',
    schema = 'INFORMATION_SCHEMA'
    )

cs = ctx.cursor()

cs.execute("select current_version(), current_user(), current_region()")
one_row = return cs.fetchall()
streamlit.dataframe(one_row)
cs.close()
