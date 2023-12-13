import streamlit as st

st.set_page_config(
    page_title="周益葳-履歷",
    page_icon=":rocket:",
    layout="wide",
    initial_sidebar_state="expanded"
)

content2 = """
我的寵物
"""
st.title(content2)

col1, empty_col, col2 = st.columns([1.5, 0.5, 1.5])

pets_files = ["pets/1.jpg", "pets/2.jpg", "pets/3.jpg", "pets/4.jpg", "pets/5.jpg", "pets/6.jpg"]
with col1:
    for photo in pets_files[:3]:
            st.image(photo)

with col2:
    for photo in pets_files[3:]:
            st.image(photo)
