import streamlit as st
import requests

st.title("🏏 IPL AI Match Predictor")
st.caption("Powered by Machine Learning + FastAPI")

team1 = st.selectbox("Team 1", ["MI", "CSK", "RCB"])
team2 = st.selectbox("Team 2", ["MI", "CSK", "RCB"])
venue = st.selectbox("Venue", ["Home", "Away"])

venue_val = 1 if venue == "Home" else 0

if st.button("Predict"):
    if team1 == team2:
        st.error("Select different teams")
    else:
        try:
            with st.spinner("Predicting..."):
                res = requests.get(
                    f"http://api:8000/predict?team1={team1}&team2={team2}&venue={venue_val}"
                )
                
                # 🔥 IMPORTANT: check if request worked
                res.raise_for_status()
                data = res.json()

            st.success(f"🏆 Predicted Winner: {data['predicted_winner']}")
            st.metric("Win Probability", f"{data['win_probability']}%")

        except requests.exceptions.RequestException as e:
            st.error("⚠️ API not reachable")
            st.text(str(e))