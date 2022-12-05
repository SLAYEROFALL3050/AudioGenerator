import streamlit as st

from MusicModel.music import gen_audio
# --------------------------- VARIABLES


# --------------------------- TITLE
st.title("Audio Generation Using MuseGan")

# --------------------------- MAIN
st.write("Click the Button to Generate Audio")

# SENTENCE BASED 
if st.button("GENERATE"):
    st.write("Here is the Generated Audio:")
    st.write(gen_audio())
