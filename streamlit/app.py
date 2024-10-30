import streamlit as st

name= st.text_input("enter ur name ")
if name:
    st.write(name)