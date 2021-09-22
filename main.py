import streamlit as st
import numpy as np
from pandas import DataFrame
'''
# Test auto deploy streamlit app.
'''

f = st.slider(label='f:', min_value=1, max_value=10)
x = np.linspace(0, 6, 1000)
y = np.sin(f * x)
data = np.array([x, y]).transpose()
df = DataFrame(data, columns=['x', 'y']).set_index('x')
st.line_chart(data=df)
