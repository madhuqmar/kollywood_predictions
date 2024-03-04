import streamlit as st

st.title("Kollywood Predictions")

directors = ["PA Ranjith", "Aishwarya Rajinikanth"]
selected_bet_amount = st.selectbox("Select a director", directors)