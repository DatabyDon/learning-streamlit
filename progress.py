import streamlit as st
import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'{i+1}%') # I changed it to a percent
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'