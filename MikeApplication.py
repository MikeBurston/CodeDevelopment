import streamlit
import pandas

streamlit.text('Hello World')

my_fruit_list = pandas.read_csv("https://api.nal.usda.gov/fdc/v1/foods/list?api_key=gWioEyTJ4azAEr6PQm4slHxqU2CzzBln9JmoCf93")

streamlit.dataframe(my_fruit_list)
