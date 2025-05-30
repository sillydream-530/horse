import streamlit as st
import pandas as pd
from estimator import estimate_win_probabilities
import altair as alt

st.set_page_config(page_title="香港賽馬勝率估計", page_icon="🏇")
st.title("🏇 香港賽馬勝率估計系統")

uploaded_file = st.file_uploader("請上傳馬匹資料（CSV格式）", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    try:
        result_df = estimate_win_probabilities(df)
        st.subheader("📊 勝率估算結果")
        st.dataframe(result_df, use_container_width=True)

        st.subheader("📈 視覺化圖表")
        chart = alt.Chart(result_df).mark_bar().encode(
            x=alt.X("馬名", sort="-y"),
            y="估計勝率",
            color="馬名"
        )
        st.altair_chart(chart, use_container_width=True)
    except Exception as e:
        st.error(f"處理資料時發生錯誤：{e}")
else:
    st.info("請上傳包含以下欄位的CSV檔案：馬名、騎師勝率、練馬師勝率、近五場名次、近五場出馬數、賠率")