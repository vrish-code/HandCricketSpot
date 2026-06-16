import random
import streamlit as st
import matplotlib as plt
import pandas as pd

st.set_page_config(layout="wide")

if "playDict" not in st.session_state:
    st.session_state.playDict={"Score":0,
              "BallsPlayed":0,
              "RunRate":0 }
if "playerName" not in st.session_state:
    st.session_state.playerName=f"Player{random.randint(1000,10000)}"
def playingInterface():
    

    with st.container(border=True):
        choiceMatch=st.slider("How many overs for the match?", min_value=1, max_value=20, value=5)
        choiceMatch*=6
        
       
        c1,c2=st.columns(2, border=True)  
        with c1:
            st.badge("Batting", color="green")
            st.subheader(st.session_state.playerName)
            st.divider()
            st.image(r"images/humanIm.png.png")
        with c2:
            st.badge("Bowling", color="red")
            st.subheader("Bot")
            st.divider()
            st.image(r"images/robotImg.png")
            
            
        with st.container(border=True):
            st.subheader("Play here.")
            c1,c2=st.columns(2, border=True)
            with c1:
                st.badge(st.session_state.playerName, color="blue")
                st.write(f"Player to Bat")
                runPlayed=st.slider("Choose what to play.", min_value=1, max_value=11)
                if runPlayed:
                    st.session_state.playDict["Score"]+=runPlayed
                    st.session_state.playDict["BallsPlayed"]+=1
                    st.session_state.playDict["RunRate"]=st.session_state.playDict["Score"]//st.session_state.playDict["BallsPlayed"]
                  
            with c2:
                st.badge("Bot", color="green")
                st.write(f"Bot to {"Bowl"}")
                if runPlayed:
                    runPlayedByBot=random.choice(list(range(1,11)))
          
            if runPlayed and runPlayedByBot:
                with st.container(border=True):
                    st.write(f"Player:{runPlayed}")
                    st.write(f"Bot: {runPlayedByBot}")
                    if runPlayed==runPlayedByBot:
                          with c1:
                            st.error("Out!")
                            st.subheader("Game Stats")
                            st.divider()
                            with st.container(border=True):
                                if st.button("Quit"):
                                    choice=st.pills("Are your ")
                                c9,c0,ca=st.columns(3, border=True)
                                c9.metric("Score", f"{st.session_state.playDict["Score"]} RUNS")
                                c0.metric("Run Rate", f"{st.session_state.playDict["RunRate"]}")
                                ca.metric("Overs Played", f"{st.session_state.playDict["BallsPlayed"]} OVERS")
                            
                    elif st.session_state.playDict["BallsPlayed"]==choiceMatch:
                        st.success("Match finished!")
                        st.subheader("Game Stats")
                        st.divider()
                        with st.container(border=True):
                          c9,c0,ca=st.columns(3, border=True)
                          c9.metric("Score", f"{st.session_state.playDict["Score"]} RUNS")
                          c0.metric("Run Rate", f"{st.session_state.playDict["RunRate"]}")
                          ca.metric("Overs Played", f"{st.session_state.playDict["BallsPlayed"]//6} OVERS")
                    else:
                        st.subheader("Game Stats")
                        st.divider()
                        with st.container(border=True):
                          c9,c0,ca=st.columns(3, border=True)
                          c9.metric("Score", f"{st.session_state.playDict["Score"]} RUNS")
                          c0.metric("Run Rate", f"{st.session_state.playDict["RunRate"]}")
                          ca.metric("Overs Played", f"{st.session_state.playDict["BallsPlayed"]//6} OVERS")
                    

playingInterface()
