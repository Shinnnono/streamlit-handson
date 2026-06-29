import streamlit as st

#入力欄とボタン
st.title("📝 TODOアプリ")

task = st.text_input("タスクを入力")

if st.button("追加"):
   st.write(f"{task}")
tasks = [] // task = st.text_input("タスクを入力")の行に上書き

#step2:リストに入力
task = st.text_input("タスクを入力")
if st.button("追加"):
   tasks.append(task) // append()はリストに値を追加する関数
   st.write(f"{task}")

st.write("### タスク一覧")
st.write(tasks)
