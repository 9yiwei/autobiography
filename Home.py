import streamlit as st

st.set_page_config(
    page_title="汪喵星球-測試工程師",
    page_icon=":rocket:",
    layout="wide",
    initial_sidebar_state="expanded"
)

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", use_column_width="auto")

with col2:
    st.title("周益葳 - Howard")
    content1 = """
您好，我叫做周益葳(60%汪星人、40%喵星人)，來自朝陽科技大學資訊管理系，興趣是看動畫、打遊戲、爬山等等。 \n
我的上一份(正職)工作是軟體專案助理，讓我了解了程式開發流程，由於工作需要，我需要進行網站測試並記錄Bug，準備相關測試文件等。
也因為上一份工作的要求，我還需要將客戶或主管的要求精簡化，讓接收訊息的人能夠用迅速的理解問題。
之前也因為工作中程式上線後有短暫駐點，需要直接的面對客戶，能以使用者的角度看待需求，也學會了靈機應變和獨立作業的能力。 \n
想要到貴公司上班的原因是因為想要帶家裡的狗、貓一起上班，也喜歡公司的文化、想要為毛小孩們出一份力，也希望能在程式上面更加進步。
    """
    st.info(content1)

content2 = """
工作經歷(3-4年)
"""
st.title(content2)

content3 = """
2022/07－現在 \n
任職-良品餐飲公司（因家人私人因素幫忙代班） \n
因為是幫忙代班，工作內容比較簡單，所以比較有時間規劃自己的時間，目前程式皆使用Udemy自學Python，完成課程如下: \n
1.100 Days of Code: The Complete Python Pro Bootcamp for 2023 \n
2.Python Mega Course: Learn Python in 60 Days, Build 20 Apps \n
3.Selenium Webdriver with PYTHON from Scratch + Frameworks \n
從課程中不但了解程式前後端的開發邏輯、自動化的測試方法，也希望之後能朝自動化測試的方向前進，除此之外有空閒之餘也會上LeetCode刷題。
"""
st.write(content3)
st.divider()

content4 = """
2020/05－2022/05 \n
任職-桓基科技(軟體專案助理) \n
主要負責團隊的專案協調、時間控管、系統測試、專案文件製作整合的工作，也時常與團隊成員討論使用者需求、議題，也時常參與使用者需求訪談及規劃往後會議。
"""
st.write(content4)
st.divider()

content5 = """
2019/10－2020/02 \n
任職-東慧(人資)
"""
st.write(content5)
st.divider()
