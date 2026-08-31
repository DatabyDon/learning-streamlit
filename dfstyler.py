import streamlit as st
import numpy as np
import pandas as pd # Added in V2

dataframe = np.random.randn(10,20)

# This 'draws' a dataframe
st.dataframe(dataframe)

# V2

# Now we'll use pandas and a Styler from Streamlit
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

# Using a Styler, we can highlight the max value in each column
st.dataframe(dataframe.style.highlight_max(axis=0))