# 香港賽馬勝率估計系統 🏇

本系統會根據賠率、騎師勝率、練馬師勝率，以及馬匹最近五場成績（按場內出馬數計算）來預估勝率。

## 安裝方式

```bash
git clone https://github.com/YOUR_USERNAME/horse_racing_win_estimator.git
cd horse_racing_win_estimator
pip install -r requirements.txt
streamlit run app.py
```

## 輸入CSV欄位格式
- 馬名
- 騎師勝率（0～1）
- 練馬師勝率（0～1）
- 近五場名次（例如："2 1 4 3 1"）
- 近五場出馬數（例如："12 14 14 13 12"）
- 賠率（小數）