import streamlit as st


st.header("What is ur name")
name = st.text_input("Enter Your name")

# Subheader
st.checkbox("Male")
st.checkbox("Female")

if st.button("Submit") and len(name)>0:
    st.write(f'Hi {name}, you are ...')