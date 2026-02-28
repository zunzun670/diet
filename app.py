import streamlit as st

# アプリのタイトル
st.title("ぴよぴよの1年後の素敵な姿への道🐣")

# 1. プルダウンリスト（セレクトボックス）
# 最初の選択肢を空にするか、案内文にします
option = st.selectbox(
    'メニューを選んでね',
    ['--', 
     '朝ごはんのオススメ', 
     '太もも引き締め', 
     '二の腕シェイプ', 
     'お腹凹ませ']
)

# 2. 下部の表示エリア（枠線付き）
st.write("---") # 区切り線

# 枠（container）の中に結果を表示
with st.container(border=True):
    if option == '朝ごはんのオススメ':
        st.write("### 納豆🍚")
        st.caption("タンパク質で代謝のスイッチをオン！")
    
    elif option == '太もも引き締め':
        st.write("### 内ももピタッと閉じ（1分）")
        st.caption("デスクワーク中もこっそりトレーニング！")
        
    elif option == '二の腕シェイプ':
        st.write("### 腕を後ろに引いて歩く")
        st.caption("通勤の1万歩が二の腕痩せタイムに！")
        
    elif option == 'お腹凹ませ':
        st.write("### おへそを背骨に近づける（ドローイン）")
        st.caption("信号待ちの間にこっそりお腹を凹ませて！")
        
    else:
        st.write("メニューを選んでください👆")
