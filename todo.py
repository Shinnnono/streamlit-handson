import streamlit as st

#入力欄とボタン
st.title("📝 TODOアプリ")

task = st.text_input("タスクを入力")

if st.button("追加"):
   st.write(f"{task}")
st.session_state.tasks = []

#step2:リストに入力
task = st.text_input("タスクを入力")
if st.button("追加"):
   tasks.append(task) // append()はリストに値を追加する関数
   st.write(f"{task}")

st.write("### タスク一覧")
st.write(tasks)

#step3:session_stateを追加
if "tasks" not in st.session_state:
   st.session_state.tasks = []

task = st.text_input("タスクを入力")
if st.button("追加"):
   st.session_state.tasks.append(task)

st.write("### タスク一覧")
st.write(st.session_state.tasks)
