import streamlit as st

st.title("ペット当番アプリ（ver1）")

# メンバー登録ブロック
st.header("① 当番メンバーを登録しよう！！")

# デフォルトの4人（あとで追加/削除できるようにする予定）
default_members = ["A", "B", "C", "D"]
members = st.text_input("当番メンバー（カンマで区切ってね）", ", ".join(default_members))

# 入力したメンバーをリストに変換
member_list = [m.strip() for m in members.split(",") if m.strip()]

st.write("登録されたメンバー一覧：", member_list)

import pandas as pd
from datetime import date

# 日付生成（今月1日〜30日）
days = [f"{i}日" for i in range(1, 31)]

# 空の当番表データフレーム
schedule_df = pd.DataFrame({
    "日付": days,
    "餌やり当番": [""] * 30,
    "散歩当番": [""] * 30
})

# 表示
st.header("② 今月の当番カレンダー")
st.dataframe(schedule_df)
