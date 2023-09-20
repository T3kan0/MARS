#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  19 08:37:00 2021

@author: nt4-nani
"""


import streamlit as st
import pandas as pd
import time
from PIL import Image

st.set_page_config(
    page_title="MARS",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

z, astep, logo = st.columns([0.52, 0.38, 0.25])
with z:
    st.image('https://github.com/T3kan0/mars/blob/main/MARSv1.01/reg.png', width=250)
with astep:
    st.markdown("<h1 style='text-align: left; color: darkred;'>A-STEP</h1>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: left; color: grey;'>🧑🏼‍🎓 👨🏽‍🎓Supplemental</h6>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: left; color: grey;'>Instruction (UFS)👨🏽‍🏫</h6>", unsafe_allow_html=True)    
with logo:
    st.image('https://github.com/T3kan0/mars/blob/main/MARSv1.01/reg.png', width=250)
st.markdown("<h2 style='text-align: center; color: grey;'>Merging Attendance RegisterS (MARS)</h2>", unsafe_allow_html=True)
st.write("<h4 style='text-align: center; color: grey;'>version: 1.0.</h4>", unsafe_allow_html=True)
col1, col2 = st.columns([2,1], gap='small')
with col1:
    st.image('https://github.com/T3kan0/mars/blob/main/MARSv1.01/logo3.png')
with col2:
    st.write('Welcome to the A-STEP Web Application **MARS** v.1.0. This was developed for the merging of large weekly\
 attendance files for the A-STEP data intern team, as part of their weekly data pre-processing operations.')
    genre = st.radio(
    ":red[**How Would You Like MARS to Combine Your Files?**]💡",
    [":rainbow[**Concatinate**]", ":rainbow[**Right Join**]", ":rainbow[**Left Join:**]"],
    captions = ["Default: Stacking Files Atop One Another 📕📗📘➡️📚",
                "Combines Files Based on Columns in the Right File 👉🏾", "Combines Files Based on Columns in the Left File 👈🏾"])
st.sidebar.markdown("<h1 style='text-align: center; color: grey;'>Centre for Teaching and Learning</h1>", unsafe_allow_html=True)
#img = Image.open('https://github.com/T3kan0/mars/blob/main/MARSv1.01/logio.jpeg')
st.sidebar.image('https://github.com/T3kan0/mars/blob/main/MARSv1.01/logio.jpeg')

bulk_files = st.sidebar.file_uploader('Upload Files',
                                     type=['xlsx', 'csv'],
                                     accept_multiple_files=True)
    
col3, col4 = st.columns([.90,0.10], gap='small')
if 'column_choice' not in st.session_state:
    st.session_state['column_choice'] = 'SUBJECT'
if bulk_files:
    st.sidebar.success('File Uploaded', icon="✅")
if bulk_files is not None:
    n_files = []
    Names = []
    Sub = []
    Cat_Nb = []
    edited_files = []
    for j, uploaded_file in enumerate(bulk_files):
        if uploaded_file.type == 'text/csv':
            bytes_data = pd.read_csv(uploaded_file, sep=',')
            col_name = uploaded_file.name
            sub = col_name[0:4]
            cat = col_name[4:8]
            n_files.append(bytes_data)
            Names.append(col_name)
            Sub.append(sub)
            Cat_Nb.append(cat)
        else:
            bytes_data = pd.read_excel(uploaded_file)
            n_files.append(bytes_data)
            
    if len(n_files) == 1:
        with col3:
            st.write(':blue[Register ]',j+1)
            col3.write(bytes_data.head(3))
            col_n1 = bytes_data.columns
        with col4:
            st.write(':blue[Type : ]',uploaded_file.type)
            st.image('https://github.com/T3kan0/mars/blob/main/MARSv1.01/tech.png', width=130)  
    elif len(n_files) >=2:
        col5, col6 = st.columns([.90, 0.10], gap='small')
        with col3:
            st.write(':blue[Register ]', j)
            col3.write(n_files[0].head(2))
            col_n1 = n_files[0].columns
        with col4:
            st.write(':blue[Type : ]',uploaded_file.type)
            st.image('https://github.com/T3kan0/mars/blob/main/MARSv1.01/tech.png', width=120)
        with col5:
            st.write(':blue[Register ]',j+1)
            col5.write(n_files[1].head(2))
            col_n2 = n_files[1].columns
        with col6:
            st.write(':blue[Type : ]', uploaded_file.type)
            st.image('https://github.com/T3kan0/mars/blob/main/MARSv1.01/tech.png', width=120)

              
    st.write(':blue[Number of Files Uploaded : ]', len(n_files))
    editer, selector, adder, explainer = st.columns([.30, .20, .20, 0.30], gap='small')
    with editer:   
        edits = st.radio(
    ":red[**How Would You Like MARS to Edit Your Files?**]💡",
    [":rainbow[**Add Columns**]", ":rainbow[**Remove Columns**]",":rainbow[**Change Column Names**]"],
        captions = ["Make a new column in the data files 👨🏽‍🔧",
                "Filter data files by column names 👩🏽‍🔧",
                "Edit column names in data files 🛠️"])
    with selector:
        if edits == ":rainbow[**Add Columns**]":
            if len(n_files) == 0:
                st.write(' ')
            elif len(n_files) >=1:
                Add_more = st.button(':red[Add Columns:]')
                st.write(':orange[This option will add two more columns to the uploaded data files 👉🏾: ]')
    with adder:
         if edits == ":rainbow[**Add Columns**]":
            if len(n_files) == 0:
                st.write(' ')
            elif len(n_files) >=1:
                clm_dic = {'SUBJECT': Sub,
                           'CATALOG NBR': Cat_Nb}
                clm_df = pd.DataFrame.from_dict(clm_dic)
                st.write(clm_df.head(4))
    with explainer:
         if edits == ":rainbow[**Add Columns**]":
            if len(n_files) == 0:
                st.write(' ')
            elif len(n_files) >=1:
                if Add_more:
                    edited_files = []
                    for files, clm, clm_ent in zip(n_files, clm_df['SUBJECT'], clm_df['CATALOG NBR']):                        
                        files['SUBJECT'] = clm
                        files['CATALOG NBR'] = clm_ent
                        edited_files.append(files)
                        bulk = files.to_csv()
                    with st.spinner('Wait for it...'):
                        time.sleep(3)
                    st.success('Colums Successfully Added!', icon="✅")
                else:
                   st.write(' ')
    if len(n_files) == 0:
        st.write(' ')
    elif len(n_files) >=1:
        if edits == ":rainbow[**Add Columns**]":
            if Add_more:                               
                st.write(':blue[Register ]',j)
                st.write(edited_files[0].head(3))
    if edits == ":rainbow[**Remove Columns**]":
        with selector:
            if len(n_files) == 0:
                st.write(' ')
            elif len(n_files) >=1:
                Rem_more = st.button(':red[Remove Columns:]')
                st.write(':orange[This option will remove columns from the uploaded data files 👉🏾: ]')

        with adder:
            if len(n_files) == 0:
                st.write(' ')
            elif len(n_files) >=1:
                dtt = pd.read_csv('bulk_file.csv')
                lis = dtt.columns
                column_name = st.multiselect(
                    ':blue[Select Column Name: ⚙️]',
                     lis)
        with explainer:
            if len(n_files) == 0:
                st.write(' ')
            elif len(n_files) >=1:
                if Rem_more:
                    dropped = dtt.drop(columns=column_name)
                    progress_bar = st.progress(0)
                    for perc_completed in range(100):
                        time.sleep(0.001)
                    progress_bar.progress(perc_completed+1)
                    st.write(dropped.columns)
                    st.success('Columns Successfully Removed!', icon="✅")
    if len(n_files) == 0:
        st.write(' ')
    elif len(n_files) >=1:
        if edits == ":rainbow[**Remove Columns**]":
            if Rem_more:
                st.write(':blue[Edited File👇🏾]')
                st.write(dropped.head())
                dropped.to_csv('bulk_file1.csv')
                with open('bulk_file1.csv', "rb") as file:
                    btn = st.download_button(
                        label=":red[Download Edited File]",
                        data=file,
                        file_name='new_file',
                        mime="file/csv"
              )
                
    if edits == ":rainbow[**Add Columns**]":                
        aggreg = st.button(':red[Aggregate Files]')
        if aggreg:
            if len(n_files) == 0:
                st.error('Error❗:  No Files Uploaded 🤷🏽')
            elif len(n_files) == 1:
                st.warning(':red[Warning - Only A Single File Found ‼️]', icon="⚠️")
            elif len(n_files) >1:
                edited_files = []
                for files, clm, clm_ent in zip(n_files, clm_df['SUBJECT'], clm_df['CATALOG NBR']):
                    files['SUBJECT'] = clm
                    files['CATALOG NBR'] = clm_ent
                    edited_files.append(files)
                    new_file = pd.concat(edited_files)
                    new_f = new_file.to_csv('bulk_file.csv')
                progress_bar = st.progress(0)
                for perc_completed in range(100):
                    time.sleep(0.05)
                progress_bar.progress(perc_completed+1)
                st.write(':blue[Bulk/Aggregated File]')
                st.write(edited_files[0].head())
                #st.write(edited_files[0]['SUBJECT'].unique())
                st.success('Files Successfully Merged!', icon="✅")               
    
        if aggreg:
            with open('bulk_file.csv', "rb") as file:
                btn = st.download_button(
                    label=":red[Download Aggregated File]",
                    data=file,
                    file_name='new_file',
                    mime="file/csv"
              )
        else:
            st.write(':blue[Press Aggregate Files to Continue]')
            
    if edits == ":rainbow[**Change Column Names**]":
        if len(n_files) == 0:
            st.info(':red[ 🚩 Remember to Upload Your Files] 🚩', icon="ℹ️")
            st.write(' ')
        elif len(n_files) >=1:
            st.write(' ')
            
            with selector:
                Rename = st.button(':red[Rename Columns:]')
                st.write(':orange[This option will remove columns from the uploaded data files 👉🏾: ]')                          
            with adder:
                renam = pd.read_csv('bulk_file1.csv')
                lis = renam.columns
                column_name = st.multiselect(
                    ':blue[Select Column to Rename: ⚙️]',
                     lis)
            with explainer:
                new_name = st.multiselect(
                    ':blue[Select New Column Name: ⚙️]',
                     ['SUBJECT', 'CATALOG NBR', 'STUDENT EMPLID',
                      'TUTOR EMPLID', 'TYPE', 'DATE', 'START TIME','END TIME'])
                if Rename:
                    progress_bar = st.progress(0)
                    for perc_completed in range(100):
                        time.sleep(0.005)
                    progress_bar.progress(perc_completed+1)
                    st.success('Files Successfully Edited!', icon="✅") 
        
        if len(n_files) == 0:
            st.write(' ')
        elif len(n_files) >=1:
            if Rename:
                for New_name, Old_name in zip(new_name, column_name):
                    renam.columns = renam.columns.str.replace(Old_name, New_name)
                st.write(':blue[Edited Bulk/Aggregated File]')
                st.write(renam.head())
                renam.to_csv('final.csv')
                with open('final.csv', "rb") as file:
                    btn = st.download_button(
                        label=":red[Download Aggregated File]",
                        data=file,
                        file_name='new_file',
                        mime="file/csv"
                  )
                st.info(':red[ 🚩 Remember to Upload Your Files] 🚩', icon="ℹ️")

                
    else:    
        st.info(':red[ 🚩 Remember to Upload Your Files] 🚩', icon="ℹ️")


