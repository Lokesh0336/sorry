import streamlit as st
import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

# Set up the title for the player
st.title("🎶 My Music Player 🎶")

# Upload a music file
music_file = st.file_uploader("Upload a Music File", type=["mp3", "wav"])

# Check if file is uploaded
if music_file is not None:
    # Save uploaded file to a temporary directory
    with open("temp_music.mp3", "wb") as f:
        f.write(music_file.getbuffer())
    
    # Load the music file
    st.audio(music_file, format="audio/mp3")

    # Show control buttons
    if st.button("Play"):
        pygame.mixer.music.load("temp_music.mp3")
        pygame.mixer.music.play()
        st.success("Music is Playing 🎵")

    if st.button("Pause"):
        pygame.mixer.music.pause()
        st.warning("Music is Paused ⏸️")

    if st.button("Stop"):
        pygame.mixer.music.stop()
        st.info("Music is Stopped ⏹️")

    if st.button("Resume"):
        pygame.mixer.music.unpause()
        st.success("Music is Resumed ▶️")

# Add a volume control
volume = st.slider("Volume", 0.0, 1.0, 0.5)
pygame.mixer.music.set_volume(volume)
