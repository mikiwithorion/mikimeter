import streamlit as st

st.set_page_config(page_title="みきメーター", layout="centered")

st.title("みきメーター（ver2）")
st.write("ようこそ！これは、みき専用の進捗＆やる気メーターです！！")

progress = st.slider("今日の達成度は？", 0, 100, 50)
st.progress(progress)

if progress == 100:
    st.balloons()
    st.success("うおおおお！！！今日も最高！！！！！！！！！！！！")
