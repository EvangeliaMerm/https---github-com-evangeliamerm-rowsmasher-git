import streamlit as st
import pandas as pd
import io
import base64
import csv

def split_csv(file, limit=5000):
    """Split a CSV file into multiple files based on a row limit."""
    file_counter = 0
    data = []
    header = None

    for row in csv.reader(file):
        if not header:
            header = row
            continue

        if len(data) >= limit:
            yield file_counter, header, data
            file_counter += 1
            data = []

        data.append(row)

    if data:
        yield file_counter, header, data

def create_download_link(df, title):
    """Generate a download link for a DataFrame."""
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{title}.csv">Download {title}</a>'
    return href

def run():
    st.set_page_config(page_title="Row Smasher", page_icon="👋")
    st.write("# Welcome to the awesome Row Smasher! 👋")

    uploaded_file = st.file_uploader("Choose a file", type=['csv'], accept_multiple_files=False)

    if st.button("Submit"):
        if uploaded_file:
            for file_counter, header, data in split_csv(uploaded_file, limit=5000):
                df = pd.DataFrame(data, columns=header)
                st.markdown(create_download_link(df, f"processed_data_{file_counter}"), unsafe_allow_html=True)

            st.success("Files processed and ready for download.")
        else:
            st.warning("Please upload a file.")

if __name__ == "__main__":
    run()
