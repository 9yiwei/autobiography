import streamlit as st
import pandas

st.set_page_config(
    page_title="周益葳-履歷",
    page_icon=":rocket:",
    layout="wide",
    initial_sidebar_state="expanded"
)

content2 = """
下面是我最近做的一些Python專案。
"""
st.title(content2)

col1, empty_col, col2 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col1:
    for index, row in df[:9].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")

with col2:
    for index, row in df[9:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")

