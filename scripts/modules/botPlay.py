import random
import streamlit as st
import matplotlib as plt
import pandas as pd


def playingInterface():
    playDict={"Score":{"Player":0, "Bot":0},
              "BallsPlayed":{"Player":0, "Bot":0},
              "RunRate":{"Player":0, "Bot":0} }

    with st.container(border=True):
        choices=["Batting 🏏", "Bowling ⚾"]
        choicePlay=st.pills("What do you want to play?", choices)
        choiceMatch=st.slider("How many overs for the match?", min_value=1, max_value=20, value=5)
        
        if choicePlay  and  choiceMatch:
            choices.remove(choicePlay)
            st.write(f"{choiceMatch} overs.")
            c1,c2=st.columns(2, border=True)
            
            with c1:
             st.badge(choicePlay, color="green")
             st.subheader(f"Player{random.randint(1000,10000)}")
             st.divider()
             st.image(r"images/humanIm.png.png")
             st.divider()
             c3,c4,c5=st.columns(3, border=True)
             c3.metric("Score", f"{playDict["Score"]["Player"]} RUNS")
             c4.metric("Run Rate", f"{playDict["RunRate"]["Player"]}")
             c5.metric("Overs Played", f"{playDict["BallsPlayed"]["Player"]} OVERS")
            with c2:
              st.badge(choices[0], color="red")
              st.subheader("Bot")
              st.divider()
              st.image(r"images/robotImg.png")
              st.divider()
              c6,c7,c8=st.columns(3, border=True)
              c6.metric("Score", f"{playDict["Score"]["Bot"]} RUNS")
              c7.metric("Run Rate", f"{playDict["RunRate"]["Bot"]}")
              c8.metric("Overs Played", f"{playDict["BallsPlayed"]["Bot"]} OVERS")\
            
            with st.container(border=True):
                st.subheader("Play here.")
                c1,c2=st.columns(2, border=True)
                with c1:
                  st.badge("Player", color="blue")
                  st.write(f"Player to {choicePlay}")
                  runPlayed=st.pills("Choose what to play.", list(range(1,11)))
                with c2:
                   st.badge("Bot", color="green")
                   st.write(f"Bot to {choices[0]}")
                   runPlayer=None

playingInterface()