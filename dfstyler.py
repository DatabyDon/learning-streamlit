import streamlit as st
import numpy as np


dataframe = np.random.randn(10,20)

# This 'draws' a dataframe
st.dataframe(dataframe)
