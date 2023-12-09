
import  streamlit as st
import os

def disable(b):
    st.session_state["disabled"] = b

        


def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)
