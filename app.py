import streamlit as st
import random

# アプリのタイトル
st.title("ぴよぴよの素敵な1年後の姿への道🐣")

# データの準備
recommendations = {
    "朝ごはんのオススメ": ["納豆🍚", "ゆで卵🥚", "ギリシャヨーグルト🥣", "オートミール粥🌾"],
    "太もも引き締め": ["ワイドスクワット 15回", "内ももピタッと閉じ（1分）", "大股歩き"],
    "二の腕シェイプ": ["後ろに腕を引いて歩く", "壁プッシュアップ", "デスク押し（5秒）"]
}

# ①プルダウンリスト（セレクトボックス）
option = st.selectbox(
    '知りたいアドバイスを選んでね',
    list(recommendations.keys())
)

# ②下部の枠内に表示
st.subheader("今日のアドバイス：")
with st.container(border=True): # 枠線を表示
    # 選択されたリストからランダムで1つ表示（または全部表示も可能）
    result = random.choice(recommendations[option])
    st.write(f"### {result}")

# 応援メッセージ
st.info("50kg達成まで、一歩ずつ進みましょう！")
