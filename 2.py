import streamlit as st

st.title("Számológép")
st.write("---")

num1 = st.number_input(label = "Első szám:")
num2 = st.number_input(label = "Második szám:")
muvelet = st.radio("Műveletek", ("összeadás", "kivonás", "szorzás", "osztás"))
ans = 0
def kiszámolás():
    if muvelet == "összeadás":
        ans == num1 + num2
    elif muvelet == "kivonás":
        ans == num1 - num2
    elif muvelet == "szorzás":
        ans == num1 * num2
    elif muvelet == "osztás" and num2!=0:
        ans == num1 / num2
    else:
        st.warning("Valami elromlott :/")

st.success(f"A végeredmény: {ans}")
asd = st.button("Kalkulálj!")
if asd:
    kiszámolás()
