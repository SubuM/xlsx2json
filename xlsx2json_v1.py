
import streamlit as st
import pandas as pd


def conv2json(data_df):
    data_json = data_df.to_json()
    st.download_button(label='Download converted JSON', data=data_json, file_name='conv_Data.json',
                       mime='application/json')


def getFile():
    # randomizing icon
    st.set_page_config(page_title='Convert XLSX to JSON', page_icon='page_facing_up', initial_sidebar_state='auto')

    # hide hamburger menu and footer
    hide_st_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    </style>
                    """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    file = st.file_uploader('Upload the excel file', type=['xls', 'xlsx'], help='Excel File Upload')
    if file:
        data_df = pd.read_excel(file, engine='openpyxl')
        conv2json(data_df)


if __name__ == '__main__':
    getFile()

