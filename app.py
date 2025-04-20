import streamlit as st
import pandas as pd

st.title("📚 دریافت اطلاعات شماره صندلی دانشجو")

# 🔐 تشخیص ادمین با رمز
admin_code = st.text_input("اگر ادمین هستید رمز را وارد کنید:", type="password")

# اگر رمز درست وارد شد
if admin_code == "1234":
    st.subheader("📁 بارگذاری فایل اکسل (فقط ادمین)")
    uploaded_file = st.file_uploader("فایل اکسل را بارگذاری کنید", type=["xlsx"])
    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        st.session_state['df'] = df
        st.success("فایل جدید با موفقیت بارگذاری و جایگزین شد ✅")

# اگر فایل بارگذاری شده
if 'df' in st.session_state:
    df = st.session_state['df']

    # ورود شماره دانشجویی
    student_id = st.text_input("شماره دانشجویی خود را وارد کنید:")

    if student_id:
        results = df[df['شماره دانشجويي'].astype(str) == student_id]

        if not results.empty:
            st.success(f"نتایج برای شماره دانشجویی {student_id}:")
            st.dataframe(results[['نام درس', 'کد درس', 'ساختمان', 'شماره صندلي']])
        else:
            st.warning("شماره دانشجویی مورد نظر یافت نشد.")
else:
    st.info("لطفاً ابتدا فایل اکسل توسط ادمین بارگذاری شود.")
