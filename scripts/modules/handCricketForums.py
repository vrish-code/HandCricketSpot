import streamlit as st
import apiFunctions as apf


def newArticle():
    with st.container(border=True):
        name=st.text_input("Enter your name.")