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
        # Dynamic slider for choosing overs
        choiceMatchBow = st.slider(
            "How many overs for the match?", 
            min_value=1, 
            max_value=20, 
            key="initial_overs_slider"
        )
        play = st.button(
            f"Play match for {choiceMatchBow} overs", 
            key="initial_play_match_button"
        )
        if play:
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
        # Unique keys assigned to all layout blocks and interaction triggers
        with st.container(border=True, key="team_status_container"):
            c1, c2 = st.columns(2, border=True, key="team_status_columns")  
            with c1:
                st.badge("Bowling", color="green", key="bowling_status_badge")
                st.subheader(st.session_state.playerName)
                st.divider()
                st.image(r"images/humanIm.png.png")
            with c2:
                st.badge("Batting", color="red", key="batting_status_badge")
                st.subheader("Bot")
                st.divider()
                st.image(r"images/robotImg.png")
            
        with st.container(border=True, key="main_gameplay_container"):
            st.subheader("Play here.")
            with st.container(border=True, key="quit_button_container"):
                if st.button("Quit this page", key="quit_game_session_button"):
                    st.session_state.clear()
                    st.rerun()
                    playingInterface()
                        
            c1, c2 = st.columns(2, border=True, key="gameplay_action_columns")
            
            # Use stateful variables to hold button context safely across re-renders
            play = False
            
            with c1:
                st.badge(st.session_state.playerName, color="blue", key="player_turn_badge")
                st.write("Player to Bowl")
                st.warning("Please don't use this playing system after you get out or after the match is over.")
                
                # Append total ball history string length to keep keys unique for every turn
                ball_suffix = f"_ball_{st.session_state.playDict['Balls Played']}"
                runPlayed = st.slider(
                    "Choose what to play.", 
                    min_value=1, 
                    max_value=11, 
                    key=f"player_runs_slider{ball_suffix}"
                )
                if st.button(f"Play {runPlayed}?", key=f"submit_run_button{ball_suffix}"):
                    play = True
                    st.session_state.playDict["Balls Played"] += 1
                  
            with c2:
                st.badge("Bot", color="green", key="bot_turn_badge")
                st.write("Bot to Bat")
                if play: 
                    runPlayedByBot = random.choice(list(range(1, 12)))
                    st.metric("Run played by bot", runPlayedByBot)
                    st.session_state.playDict["Runs Played"].append(runPlayed)
                    st.session_state.playDict["Score"] += runPlayed
                    st.session_state.playDict["RunRate"] = st.session_state.playDict["Score"] // st.session_state.playDict["Balls Played"]
          
            if play and 'runPlayedByBot' in locals():
                # Post-ball resolution container tracking
                resolution_suffix = f"_res_{st.session_state.playDict['Balls Played']}"
                
                st.subheader("Game Stats")
                st.divider()
                with st.container(border=True, key=f"stats_metrics_container{resolution_suffix}"):
                    c9, c0, ca, c = st.columns(4, border=True, key=f"metrics_row_columns{resolution_suffix}")
                    c9.metric("Score", f"{st.session_state.playDict['Score']} RUNS")
                    c0.metric("Run Rate", f"{st.session_state.playDict['RunRate']}")
                    ca.metric("Balls Played", f"{st.session_state.playDict['Balls Played']} BALLS")
                    c.metric("Total overs in this match", f"{st.session_state.playDict['Total Overs']} OVERS")
                    
                with st.container(border=True, key=f"score_comparison_container{resolution_suffix}"):
                    st.write(f"Player: {runPlayed}")
                    st.write(f"Bot: {runPlayedByBot}")
                    
                    if runPlayed == runPlayedByBot:
                        st.error("Out!")
                        st.divider()
                        with st.container(border=True, key=f"out_dataframe_container{resolution_suffix}"):
                            gameStats = pd.DataFrame(list(st.session_state.playDict.items()), columns=["Stat Category", "Stat Obtained"])
                            st.dataframe(gameStats, hide_index=True, key=f"out_stats_table{resolution_suffix}")
                            st.divider()
                            
                            with st.container(border=True, key=f"out_chart_container{resolution_suffix}"):
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
                                
                            t.sleep(5)  # Reduced from 50 seconds to keep server context active
                            st.session_state.clear()
                            st.rerun()
                          
                    elif st.session_state.playDict["Balls Played"] == st.session_state.playDict["Total Overs"] * 6:
                        st.success("Match finished!")
                        st.subheader("Game Stats")
                        st.divider()
                        st.session_state.gameOver = True
                        with st.container(border=True, key=f"finish_dataframe_container{resolution_suffix}"):
                            gameStats = pd.DataFrame(list(st.session_state.playDict.items()), columns=["Stat Category", "Stat Obtained"])
                            st.dataframe(gameStats, hide_index=True, key=f"finish_stats_table{resolution_suffix}")
                            st.divider()
                            
                            with st.container(border=True, key=f"finish_chart_container{resolution_suffix}"):
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
