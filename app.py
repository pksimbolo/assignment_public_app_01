# -*- coding: utf-8 -*-

import streamlit as st
from datetime import datetime
from datetime import date

st.title("User Information")

name = st.text_input("Name")

min_date = date(1923, 1, 1)
today = datetime.today()

birth_date = st.date_input("Date of Birth", min_value=min_date, max_value=today)

age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

sex = st.selectbox("Sex", ["Male", "Female", "Other"])

st.text(f"Name: {name}")
st.text(f"Age: {age}")
st.text(f"Sex: {sex}")


number1 = st.number_input("Number 1 (Min 200, Max 400)", min_value=200, max_value=400)
number2 = st.number_input("Number 2 (Min 100, Max 200)", min_value=100, max_value=200)

st.text(f"Sum is {number1+number2}")

st.text(f"Multipy is {number1*number2}")

st.text(f"Substract is {number1-number2}")

st.text(f"Divided is {number1/number2}")
