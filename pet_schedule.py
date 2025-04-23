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
