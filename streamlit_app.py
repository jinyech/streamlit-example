from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to 简政!
简政是一个提供全面政策信息、提供专业政策建议的一体化平台。
我们的愿景是“让数据意识普及，让智能工具惠民，让政府信息更加亲民”
"""
wordword=open("浙江省保障性住房解疑.txt","r",encoding='utf-8').read()
if st.button('保障性住房解疑'):
   st.write(wordword)
