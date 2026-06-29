import streamlit as st

st.title("👋挨拶アプリ")

name=st.text_input("名前を入力")

if st.button("挨拶する"):
    st.write(f"### こんにちは、{name}さん!")
