from tkinter import Label
import streamlit as st
import pandas as pd
import numpy as np
import sys
from logic import logic
# from streamlit_option_menu import option_menu
from scipy.misc import electrocardiogram
import matplotlib.pyplot as plt
import time
from collections import namedtuple, defaultdict

st.set_page_config(
    page_title='Sampling Studio',
    page_icon="chart_with_upwards_trend",
    layout='wide'
)

hide_st_style = """
            <style>
            # MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


local_css("style.css")


st.title(" Welcom to Sampling Studio")


@st.cache(allow_output_mutation=True)
def get_data():
    return []


with st.sidebar:

    st.title(':gear: Sampling Studio')
    generate_expander = st.sidebar.expander(
        "Generate/Add Signal ", expanded=False)
    Label = generate_expander.text_input("Label")
    frecq = generate_expander.text_input("Frecquency in Hz")
    Amplitude = generate_expander.text_input("Amplitude")
    Add_button_clicked = generate_expander.button("Save", key=1)

    if Add_button_clicked:
        get_data().append(
            {"Label": Label, "Frecquency in Hz": frecq, "Amplitude": Amplitude})
    Signals = pd.DataFrame(get_data())
    st.write(Signals)
    list_sig = [1,2,3,4]
    delet_button = st.button('Delete A signal')
    if delet_button:
        Deleted_Signal = st.number_input(
            "Enter the row of the Signal", min_value=0,max_value=5)
        print(Deleted_Signal)    
        # logic.remove_Signal(Deleted_Signal,list_sig)
    
        # Signals.drop([Deleted_Signal], axis=0, inplace=True)
    # st.write(Signals)
    print(list_sig)
    st.write("")

    if st.button(" Upload a Signal"):

        file = st.file_uploader("Upload Your Signal")
        Data = pd.read_csv(file)
    st.slider('Add Noise', 0, 100)

    st.button("Save")
