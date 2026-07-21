import streamlit as st
import apiFunctions as apf
import random as r
import datetime as dt


class article:
    def __init__(self, name, title, article, descr):
        self.name=name
        self.title=title
        self.article=article
        self.descr=descr
    
    def save(self):
        articleDict={r.randint(1, 100000000000000000000000000000000000000):{"Title":self.title, "Author":self.author, "Text":self.article, "Description":self.descr}}
        apf.patch(articleDict)
if "stFormKey" not in st.session_state:
    stFormKey=r.randint(1,10000)
def newArticle():
    with st.container(border=True):
        with st.form(st.session_state.stFormKey):
            st.badge("Create your article here.", color="green")
            name=st.text_input("Enter your name.")
            st.divider()
            title=st.text_input("Enter your article's title.")
            st.divider()
            article=st.textarea("Enter your article here.", height=300)
            st.divider()
            descr=st.textarea("Give a small description about your article.", height=200, max_chars=350)
            st.divider()
            submit=st.form_submit_button("Submit your article?")
        if submit:
            articleDatabase=article(name,title,article,descr)
            articleDatabase.save()
            st.success("Your article has been published to the database!")





    