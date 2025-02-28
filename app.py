import streamlit as st
from crewai import Crew
from dotenv import load_dotenv
import os
from multi_agent_story import story_crew

# Load API keys
load_dotenv()

# Streamlit UI
st.title("📖 AI-Powered Story Generator")
st.write("Create dynamic AI-generated stories using multiple AI agents!")

# User Inputs
genre = st.text_input("Enter Story Genre:", "Fantasy")
theme = st.text_input("Enter Story Theme:", "An ancient prophecy")
characters = st.text_input("Enter Characters (comma-separated):", "Elara the Mage, Dain the Warrior, Zyrith the Dark Lord")
story_length = st.selectbox("Select Story Length:", ["Short", "Medium", "Long"])

if st.button("Generate Story"):
    st.write("🚀 AI Agents are working on your story...")
    
    user_input = {
        "genre": genre,
        "theme": theme,
        "characters": characters,
        "story_length": story_length
    }

    final_story = story_crew.kickoff()
    st.subheader("📖 Your AI-Generated Story")
    st.write(final_story)

# Run Streamlit: streamlit run app.py
