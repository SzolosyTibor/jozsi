import streamlit as st

def display_power():
    power = 2 ** st.session_state.myslider
    st.write("A 2", st.session_state.myslider, "hatványa:", power)

st.slider(
    "Hatvány",
    0,
    10,
    1,
    key="myslider",
    on_change=display_power
)

