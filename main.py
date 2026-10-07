import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt
import time 
data=pd.read_csv("data/orders.csv")
# st.dataframe(data)

group_by_city=data.groupby("city")['quantity'].sum()
st.dataframe(group_by_city.reset_index([]))


st.bar_chart(group_by_city)
