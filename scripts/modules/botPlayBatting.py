import random
import streamlit as st
import matplotlib.pyplot as plt
import time as t
import pandas as pd
  

st.set_page_config(layout="wide")


def startDataBase():
    if "playerName" not in st.session_state:
     st.session_state.playerName=f"Player{random.randint(1000,10000)}"
    if "playDict" not in st.session_state:
        choiceMatch=st.slider("How many overs for the match?", min_value=1, max_value=20)
        play=st.button(f"Play match for {choiceMatch} overs")
        if play:
          choiceMatch*=6
          overCount=choiceMatch/6
          if "playDict" not in st.session_state:
            st.session_state.playDict={"Score":0,
              "Runs Played":[],
              "Balls Played":0,
              "RunRate":0,
               "Total Overs":overCount
               }
            st.rerun()

def playingInterface():
    
    startDataBase()
   
    if "playDict" in st.session_state and st.session_state.playDict:
        with st.container(border=True):
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
            with st.container(border=True):
                if st.button("Quit this page"):
                    st.session_state.clear()
                    st.rerun()
                    playingInterface()
                        
            c1,c2=st.columns(2, border=True)
            with c1:
                st.badge(st.session_state.playerName, color="blue")
                st.write(f"Player to Bat")
                st.warning("Please don't use this playing system after you get out or after the match is over.")
                runPlayed=st.slider("Choose what to play.", min_value=1, max_value=11)
                play=st.button(f"Play {runPlayed}?")
                if play:
                    st.session_state.playDict["Runs Played"].append(runPlayed)
                    st.session_state.playDict["Score"]+=runPlayed
                    st.session_state.playDict["Balls Played"]+=1
                    st.session_state.playDict["RunRate"]=st.session_state.playDict["Score"]//st.session_state.playDict["BallsPlayed"]
                  
            with c2:
                st.badge("Bot", color="green")
                st.write(f"Bot to {"Bowl"}")
                if play: 
                    
                    st.session_state.runPlayedByBot=random.choice(list(range(1,12)))
                    st.metric("Run played by bot", st.session_state.runPlayedByBot)
          
            if play and st.session_state.runPlayedByBot:
                st.subheader("Game Stats")
                st.divider()
                with st.container(border=True):
                    c9,c0,ca,c=st.columns(4, border=True)
                    c9.metric("Score", f"{st.session_state.playDict["Score"]} RUNS")
                    c0.metric("Run Rate", f"{st.session_state.playDict["RunRate"]}")
                    ca.metric("Balls Played", f"{st.session_state.playDict["BallsPlayed"]} BALLS")
                    c.metric("Total overs in this match", f"{st.session_state.playDict["Total Overs"]} OVERS")
                with st.container(border=True):
                    st.write(f"Player:{runPlayed}")
                    st.write(f"Bot: {st.session_state.runPlayedByBot}")
                    if runPlayed==st.session_state.runPlayedByBot:
                        st.error("Out!")
                        st.session_state.gameOver=True
                        st.subheader("Game Stats")
                        st.divider()
                        with st.container(border=True):
                            gameStats=pd.DataFrame(list(st.session_state.playDict.items()), columns=["Stat Category", "Stat Obtained"])
                            st.dataframe(gameStats, hide_index=True)
                            st.divider()
                            h,j=st.columns(2, border=True)
                            with h:
                             ballsBowledList=list(range(1, (st.session_state.playDict["Total Overs"]*6)+1))
                             a,b=plt.subplots()
                             b.plot(ballsBowledList, st.session_state.playDict["Runs Played"], label=st.session_state.playerName, color="blue")
                            t.sleep(50)
                            st.session_state.clear()
                            st.rerun()
                          
                    elif st.session_state.playDict["BallsPlayed"]==st.session_state.playDict["Total Overs"]*6:
                        st.success("Match finished!")
                        st.subheader("Game Stats")
                        st.divider()
                        st.session_state.gameOver=True
                        with st.container(border=True):
                          c9,c0,ca=st.columns(3, border=True)
                          c9.metric("Score", f"{st.session_state.playDict["Score"]} RUNS")
                          c0.metric("Run Rate", f"{st.session_state.playDict["RunRate"]}")
                          ca.metric("Balls Played", f"{st.session_state.playDict["BallsPlayed"]} BALLS")
                          t.sleep(50)
                          st.session_state.clear()
                          st.rerun()   
                       
                      
                  
                
                    

playingInterface()
