# https://github.com/marcoppasini/musika

# IMPORTS
from pypianoroll import Multitrack
import streamlit as st

# DOWNLOADS

# MODEL

# FINAL FUNCTION
# Spits out audio file

def gen_audio():
    to_ret = ""
    for i in range(5):
        to_ret = to_ret + str(i)

    return to_ret