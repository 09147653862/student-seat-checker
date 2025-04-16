
import streamlit as st
import pandas as pd

st.set_page_config(page_title="جستجوی شماره صندلی", layout="centered")

st.title("جستجوی شماره صندلی دانشجو")
st.markdown("لطفاً شماره دانشجویی خود را وارد کنید:")

@st.cache_data
def load_data():
    return pd.read_excel("students.xlsx")

data = load_data()

student_id = st.text_input("شماره دانشجویی:", "")

if student_id:
    result = data[data["شماره دانشجویی"].astype(str) == student_id]
    if not result.empty:
        row = result.iloc[0]
        st.success(f"دانشجو: {row['نام']} {row['نام خانوادگی']}\nشماره صندلی شما: {row['شماره صندلی']}")
    else:
        st.error("شماره دانشجویی پیدا نشد. لطفاً مجدد بررسی کنید.")
