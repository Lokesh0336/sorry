import streamlit as st

# Title of the app
st.title("💌 A Special Sorry for You 💌")

# Apology message
st.markdown("""
Hey ❤️, I messed up, and I just want to say...
""")

# Adding a button to reveal the message
if st.button("Click Here 💔"):
    st.markdown("""
    ## **SORRY** 😞
    ### I'm really sorry for what happened. 
    I didn't mean to hurt you, and I value you so much in my life. Can we start fresh and forget this? 
    🌷 *You're super important to me, and I promise to make things right!* 🌷
    """)
    st.balloons()
