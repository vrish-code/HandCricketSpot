import random
import streamlit as st
import matplotlib.pyplot as plt
import time as t
import pandas as pd

st.set_page_config(layout="wide")

def startDataBase():
    if "playerName" not in st.session_state:
        st.session_state.playerName = f"Player{random.randint(1000, 10000)}"
        
    if "playDict" not in st.session_state:
        choiceMatchBow = st.slider(
            "How many overs for the match?", 
            min_value=1, 
            max_value=20, 
            key=f"sl_i_{random.randint(10000, 99999)}"
        )
        if st.button(f"Play match for {choiceMatchBow} overs", key=f"bt_i_{random.randint(10000, 99999)}"):
            choiceMatchBow *= 6
            overCount = choiceMatchBow / 6
            st.session_state.playDict = {
                "Score": 0,
                "Runs Played": [],
                "Balls Played": 0,
                "RunRate": 0,
                "Total Overs": overCount
            }
            st.rerun()

def playingInterface():
    startDataBase()
   
    if "playDict" in st.session_state and st.session_state.playDict:
        with st.container(border=True):
            c1, c2 = st.columns(2, border=True)  
            with c1:
                st.badge("Bowling", color="green")
                st.subheader(st.session_state.playerName)
                st.divider()
                st.image(r"images/humanIm.png.png")
            with c2:
                st.badge("Batting", color="red")
                st.subheader("Bot")
                st.divider()
                st.image(r"images/robotImg.png")
            
        with st.container(border=True):
            st.subheader("Play here.")
            with st.container(border=True):
                if st.button("Quit this page", key=f"bt_q_{random.randint(10000, 99999)}"):
                    st.session_state.clear()
                    st.rerun()
                    playingInterface()
                        
            c1, c2 = st.columns(2, border=True)
            
            ball_count = st.session_state.playDict['Balls Played']
            runPlayed = st.slider("Choose what to play.", min_value=1, max_value=11, key=f"sl_p_{ball_count}_{random.randint(10000, 99999)}")
            
            if st.button(f"Play {runPlayed}?", key=f"bt_p_{ball_count}_{random.randint(10000, 99999)}"):
                st.session_state.playDict["Balls Played"] += 1
                
                with c1:
                    st.badge(st.session_state.playerName, color="blue")
                    st.write("Player to Bowl")
                    st.warning("Please don't use this playing system after you get out or after the match is over.")
                  
                with c2:
                    st.badge("Bot", color="green")
                    st.write("Bot to Bat")
                    runPlayedByBot = random.choice(list(range(1, 12)))
                    st.metric("Run played by bot", runPlayedByBot)
                    st.session_state.playDict["Runs Played"].append(runPlayed)
                    st.session_state.playDict["Score"] += runPlayed
                    st.session_state.playDict["RunRate"] = st.session_state.playDict["Score"] // st.session_state.playDict["Balls Played"]
          
                st.subheader("Game Stats")
                st.divider()
                with st.container(border=True):
                    c9, c0, ca, c = st.columns(4, border=True)
                    c9.metric("Score", f"{st.session_state.playDict['Score']} RUNS")
                    c0.metric("Run Rate", f"{st.session_state.playDict['RunRate']}")
                    ca.metric("Balls Played", f"{st.session_state.playDict['Balls Played']} BALLS")
                    c.metric("Total overs in this match", f"{st.session_state.playDict['Total Overs']} OVERS")
                    
                with st.container(border=True):
                    st.write(f"Player: {runPlayed}")
                    st.write(f"Bot: {runPlayedByBot}")
                    
                    if runPlayed == runPlayedByBot:
                        st.error("Out!")
                        st.divider()
                        with st.container(border=True):
                            gameStats = pd.DataFrame(list(st.session_state.playDict.items()), columns=["Stat Category", "Stat Obtained"])
                            st.dataframe(gameStats, hide_index=True)
                            st.divider()
                            
                            with st.container(border=True):
                                ballsBowledList = list(range(1, (int(st.session_state.playDict["Total Overs"] * 6)) + 1))
                                a, b = plt.subplots()
                                b.barh(ballsBowledList[:len(st.session_state.playDict["Runs Played"])], st.session_state.playDict["Runs Played"], color="blue")
                                b.set_title("Runs played in match")
                                b.set_xlabel("Runs played")
                                b.set_ylabel("Ball no.")
                                b.grid(True, alpha=0.06, linestyle="-")
                                if ballsBowledList:
                                    b.set_xlim(0, max(ballsBowledList))
                                st.pyplot(a)
                                
                            t.sleep(5)
                            st.session_state.clear()
                            st.rerun()
                          
                    elif st.session_state.playDict["Balls Played"] == st.session_state.playDict["Total Overs"] * 6:
                        st.success("Match finished!")
                        st.subheader("Game Stats")
                        st.divider()
                        st.session_state.gameOver = True
                        with st.container(border=True):
                            gameStats = pd.DataFrame(list(st.session_state.playDict.items()), columns=["Stat Category", "Stat Obtained"])
                            st.dataframe(gameStats, hide_index=True)
                            st.divider()
                            
                            with st.container(border=True):
                                ballsBowledList = list(range(1, (int(st.session_state.playDict["Total Overs"] * 6)) + 1))
                                a, b = plt.subplots()
                                b.barh(ballsBowledList, st.session_state.playDict["Runs Played"], label=st.session_state.playerName, color="blue")
                                b.set_title("Runs played in match")
                                b.set_xlabel("Runs played")
                                b.set_ylabel("Ball no.")
                                b.grid(True, alpha=0.06, linestyle="-")
                                if ballsBowledList:
                                    b.set_xlim(0, max(ballsBowledList))
                                st.pyplot(a)
                                
                            t.sleep(5)
                            st.session_state.clear()
                            st.rerun()   

playingInterface()
