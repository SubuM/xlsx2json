
import streamlit as st
import pandas as pd
import numpy as np
import json


def convXLSX2JSON(data_df):
    tasks = []

    for rows in data_df.index:
        names = {}
        # typecasting the refreshSchedule, as otherwise JSON cannot be serialized with int64
        params = {'refreshSchedule': int(data_df['RefreshSchedule'][rows]),
                  'subscriptionSuffix': data_df['subscriptionSuffix'][rows],
                  'Source': data_df['Source'][rows],
                  'Destination': data_df['Destination'][rows],
                  'Mode': data_df['Mode'][rows]}

        names.update({'Tasks': data_df['Tasks'][rows], 'parameters': params})
        tasks.append(names)

    extrac = {'extractions': tasks}
    json_obj = json.dumps(extrac, indent=4)

    st.download_button(label='Download JSON config', data=json_obj, file_name='config.json', mime='application/json',
                       help='Download converted config file in JSON format')


def getFile():
    # setting page icon
    st.set_page_config(page_title='Convert config file', page_icon='timer_clock', initial_sidebar_state='auto')

    # hide hamburger menu and footer logo
    hide_st_style = """
                        <style>
                        #MainMenu {visibility: hidden;}
                        footer {visibility: hidden;}
                        </style>
                        """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    inpFile = st.file_uploader(label='Upload config file in XLSX format', type='.xlsx',
                               accept_multiple_files=False,
                               help='Upload config file in .xlsx format only')

    if inpFile:
        data_df = pd.read_excel(inpFile, engine='openpyxl')
        # remove NaN with blank string, otherwise it will generate erroneous JSON
        data_df = data_df.replace(np.nan, '', regex=True)
        # call the function to convert XLSX to JSON and download the config file
        convXLSX2JSON(data_df)


if __name__ == '__main__':
    getFile()
