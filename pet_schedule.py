import streamlit as st
import calendar
from datetime import datetime, timedelta
import pandas as pd

st.title("ペット当番アプリ（ver1）")

# ① メンバー登録ブロック
st.header("① 当番メンバーを登録しよう！！！")
default_members = ["A", "B", "C", "D"]
members = st.text_input("当番メンバー（カンマで区切ってね）", ", ".join(default_members))
member_list = [m.strip() for m in members.split(",") if m.strip()]
st.write("登録されたメンバー一覧：", member_list)

# ② カレンダー表示ブロック
st.header("② 今月の当番カレンダーを見てみよう！")
today = datetime.today()
year = today.year
month = today.month
_, last_day = calendar.monthrange(year, month)
calendar_data = {}
for i in range(1, last_day + 1):
    date = datetime(year, month, i).strftime("%Y-%m-%d")
    member = member_list[(i - 1) % len(member_list)] if member_list else "未設定"
    calendar_data[date] = member
for date, member in calendar_data.items():
    st.write(f"{date}：当番 → {member}")

# ③ 散歩の当番ロジック
st.header("③ 今日の散歩はどうする？")
is_sunny = st.radio("今日の天気は？", ["晴れ", "雨"]) == "晴れ"
if "walk_queue" not in st.session_state:
    st.session_state.walk_queue = member_list.copy()
if is_sunny and st.session_state.walk_queue:
    walker = st.session_state.walk_queue.pop(0)
    st.write(f"今日の散歩当番は {walker} さんだよ！")
    st.session_state.walk_queue.append(walker)
elif not is_sunny:
    st.write("今日は雨だから、散歩はおやすみ！当番は明日にスライドするね！")
else:
    st.write("メンバーが登録されていないよ！")

# ④ スキップ処理ブロック
st.header("④ 餌やりスキップ対応（仮）")
today_index = today.day - 1
if member_list:
    todays_member = member_list[today_index % len(member_list)]
else:
    todays_member = "（未登録）"
st.write(f"今日の餌やり当番は：**{todays_member}**")
if st.button("スキップする！"):
    st.warning(f"{todays_member} さんがスキップ！")
    st.success(f"代打：{member_list[0]} さんが餌やりします！！（A担当）")
    st.info("※ 本当の順番調整は、次回のバージョンでやるよ！")

# ⑤ ペット日記ブロック
st.header("⑤ ペット日記・メモ")
diary = st.text_area("今日の様子やメモをここに書いてね！", height=150)
if st.button("メモを保存する！"):
    if diary:
        st.success("メモが保存されました！（仮）")
        st.write("**今日の記録：**")
        st.info(diary)
    else:
        st.warning("メモが空っぽだよ〜！なにか書いてから保存してね！")
