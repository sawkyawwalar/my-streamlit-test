import streamlit as st
import pandas as pd
import numpy as np
sheet = pd.read_csv('./got_deaths.csv',encoding = "ISO-8859-1")
chart_data = pd.DataFrame(
     sheet,
     columns=['death_season','death_episode','likelihoodOfReturn'])



add_selectbox = st.sidebar.selectbox(
    'Hello Choose Something',
    ('Chart', 'Video', 'Sheet')
)
if add_selectbox == 'Chart':
     st.area_chart(chart_data)
elif add_selectbox == 'Video':
     st.video('https://www.youtube.com/watch?v=w6XSQmTL2Bo')
elif add_selectbox == 'Sheet':
    st.write(sheet,500,1500)
    