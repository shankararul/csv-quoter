import streamlit as st
import pandas as pd
import csv
from pathlib import Path

st.set_page_config(layout="wide", page_title="CSV Quoter")

st.write("## Upload your unquoted csv file and quote it")
st.write(
    ":dog: Sometime CSV uploads fail if the file is unquoted. Upload your unquoted csv file to quote it. Source available [here](https://github.com/shankararul/csv-quoter/) on GitHub.")
st.sidebar.write("## Upload and Quote it :gear:")

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

def quote_file(my_upload):
    df = pd.read_csv(my_upload)
    quoted= df.to_csv(quoting=csv.QUOTE_ALL, index=False)
    st.sidebar.markdown("\n")

    st.download_button("Download Quoted file", quoted, file_name = "quoted.csv", mime="application/octet-stream", type='primary',use_container_width= True)
    st.write(df)

my_upload = st.sidebar.file_uploader("Upload your unquoted CSV File", type=["csv", "txt"])

if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
    else:
        quote_file(my_upload)
        

else:
    quote_file("./unquoted.csv")