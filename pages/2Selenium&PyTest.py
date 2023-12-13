import streamlit as st

st.set_page_config(
    page_title="周益葳-履歷",
    page_icon=":rocket:",
    layout="wide",
    initial_sidebar_state="expanded"
)

content2 = """
Selenium & pytest
"""
st.title(content2)

col1, empty_col, col2 = st.columns([1.5, 0.5, 1.5])
selenium_photo = ["selenium/selenium.jpg"]

with col1:
    for photo in selenium_photo:
        st.image(photo)
    st.write(f"[Source Code](https://github.com/9yiwei/selenium)")
with col2:
    content3 = """
1.使用Selenium WebDriver & PyTest進行網頁自動化測試 \n
(1)學習如何掌握網頁上html(id/xpath...)利用Selenium進行自動化 \n
(2)學習PyTest利用fixture建立測試執行前後設置/PageObject優化代碼 \n
(3)利用PyTest mark/params/xdist/html...將測試優化並產出報表 \n
(4)識別不同的Selenium WebDriver失敗和異常，並學習如何修復 \n
2.在Chrome、Firefox和其他瀏覽器中執行Selenium測試
"""
    st.info(content3)