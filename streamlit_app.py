from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to 简政!
简政是一个提供全面政策信息、提供
我们的愿景是“让数据意识普及，让智能工具惠民，让政府信息更加亲民”
"""

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

