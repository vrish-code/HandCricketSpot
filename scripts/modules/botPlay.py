import random
import streamlit as st
import matplotlib as plt
import pandas as pd


def playingInterface():
    with st.container(border=True):
        with st.container(border=True):
            tossChoice=st.pills("Heads or Tails?", ["Heads", "Tails"])
            coin=random.choice(["Heads", "Tails"])
            if tossChoice==coin:
                choicePlay=st.pills("Choose to?", ["Batting", "Bowling"])
            elif tossChoice!=coin:
                choicePlay=random.choice(["Batting", "Bowling"])
        c1,c2=st.columns(2, border=True)
        with c1:
            st.badge(choicePlay, color="green")
            st.subheader(f"Player{random.randint(1000,10000)}")
            st.divider()
            st.image(r"images/image.png")
            st.divider()
            st.write("Choose a number to play.")
            choicePlayed=st.pills("Choose a number", list(range(1, 11)))
        
        with c2:
            st.badge()

playingInterface()