import streamlit as st
import pandas as pd
import numpy as np 
import os
from model import recommend

st.title('냉장고 재료 기반 레시피 추천 서비스')

user_input = st.text_area('사용자가 가지고 있는 재료를 입력하세요.(ex 돼지고기, 소금, 설탕)')

if 'analysis_result' not in st.session_state:
   st.session_state['final_dataframe']= []

if 'music_result' not in st.session_state:
    st.session_state['music_result'] = pd.DataFrame()

if st.button('분석'):
    st.session_state['final_dataframe'] = recommend([user_input])

    if st.session_state['final_dataframe']:
        print(st.session_state['final_dataframe'])