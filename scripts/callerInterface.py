from modules import botPlayBatting as bpb
from modules import botPlayBowling as bpbo
import streamlit as st

def userInterface():
    st.title("Play Hand Cricket Here!")
    st.divider()
    t1,t2=st.tabs(["Batting (with bot)", "Bowling (with bot)"])
    with t1:
        bpb.playingInterface()
    with t2:
        bpbo.playingInterface()
    st.divider()
    st.info("Thank you for using my website!")
    st.caption("Vrishan Somalinga")


userInterface()