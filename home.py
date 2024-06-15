import streamlit as st

st.set_page_config(
        page_title="SeamlessVision",
        page_icon="🛒",
)


st.title("Home Page")

st.write("Welcome to SeamlessVision")

st.divider()

st.subheader(":green[Get Started]")
st.page_link("pages/instructions.py", label="See Instructions 🚀")