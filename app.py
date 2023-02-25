# -*- coding: utf-8 -*-


import streamlit as st
import pandas as pd
import numpy as np

st.write("Hello world")


df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.write(df)


dataframe = np.random.randn(5,6)
st.dataframe(dataframe)

dataframe = pd.DataFrame(
    np.random.randn(5,6),
    columns = ('col %d' % (i+1) for i in range(6))
    )
st.dataframe(dataframe.style.highlight_max(axis=0))

st.table(dataframe)

##Draw a line chart

chart_data = pd.DataFrame(np.random.randn(20,3),columns=('a','b','c'))

st.line_chart(chart_data)

#Plot a map
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

#widget

#slider
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

#text input
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

#checkbox
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

#selected box
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['second column'])

'You selected: ', option

